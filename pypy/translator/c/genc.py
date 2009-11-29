import autopath
import py
import sys, os
from pypy.translator.c.node import PyObjectNode, FuncNode
from pypy.translator.c.database import LowLevelDatabase
from pypy.translator.c.extfunc import pre_include_code_lines
from pypy.translator.llsupport.wrapper import new_wrapper
from pypy.translator.gensupp import uniquemodulename, NameManager
from pypy.translator.tool.cbuild import ExternalCompilationInfo
from pypy.rpython.lltypesystem import lltype
from pypy.tool.udir import udir
from pypy.tool import isolate
from pypy.translator.c.support import log, c_string_constant
from pypy.rpython.typesystem import getfunctionptr
from pypy.translator.c import gc

def import_module_from_directory(dir, modname):
    file, pathname, description = imp.find_module(modname, [str(dir)])
    try:
        mod = imp.load_module(modname, file, pathname, description)
    finally:
        if file:
            file.close()
    return mod

class ProfOpt(object):
    #XXX assuming gcc style flags for now
    name = "profopt"

    def __init__(self, compiler):
        self.compiler = compiler

    def first(self):
        platform = self.compiler.platform
        if platform.name == 'darwin':
            # XXX incredible hack for darwin
            cfiles = self.compiler.cfiles
            STR = '/*--no-profiling-for-this-file!--*/'
            no_prof = []
            prof = []
            for cfile in self.compiler.cfiles:
                if STR in cfile.read():
                    no_prof.append(cfile)
                else:
                    prof.append(cfile)
            p_eci = self.compiler.eci.merge(
                ExternalCompilationInfo(compile_extra=['-fprofile-generate'],
                                        link_extra=['-fprofile-generate']))
            ofiles = platform._compile_o_files(prof, p_eci)
            _, eci = self.compiler.eci.get_module_files()
            ofiles += platform._compile_o_files(no_prof, eci)
            return platform._finish_linking(ofiles, p_eci, None, True)
        else:
            return self.build('-fprofile-generate')

    def probe(self, exe, args):
        # 'args' is a single string typically containing spaces
        # and quotes, which represents several arguments.
        self.compiler.platform.execute(exe, args)

    def after(self):
        return self.build('-fprofile-use')

    def build(self, option):
        eci = ExternalCompilationInfo(compile_extra=[option],
                                      link_extra=[option])
        return self.compiler._build(eci)

class CCompilerDriver(object):
    def __init__(self, platform, cfiles, eci, outputfilename=None,
                 profbased=False):
        # XXX config might contain additional link and compile options.
        #     We need to fish for it somehow.
        self.platform = platform
        self.cfiles = cfiles
        self.eci = eci
        self.outputfilename = outputfilename
        self.profbased = profbased

    def _build(self, eci=ExternalCompilationInfo()):
        return self.platform.compile(self.cfiles, self.eci.merge(eci),
                                     outputfilename=self.outputfilename)

    def build(self):
        if self.profbased:
            return self._do_profbased()
        return self._build()

    def _do_profbased(self):
        ProfDriver, args = self.profbased
        profdrv = ProfDriver(self)
        dolog = getattr(log, profdrv.name)
        dolog(args)
        exename = profdrv.first()
        dolog('Gathering profile data from: %s %s' % (
            str(exename), args))
        profdrv.probe(exename, args)
        return profdrv.after()
    
class CBuilder(object):
    c_source_filename = None
    _compiled = False
    modulename = None
    
    def __init__(self, translator, entrypoint, config, gcpolicy=None):
        self.translator = translator
        self.entrypoint = entrypoint
        self.entrypoint_name = self.entrypoint.func_name
        self.originalentrypoint = entrypoint
        self.config = config
        self.gcpolicy = gcpolicy    # for tests only, e.g. rpython/memory/
        if gcpolicy is not None and gcpolicy.requires_stackless:
            config.translation.stackless = True
        self.eci = self.get_eci()

    def get_eci(self):
        from distutils import sysconfig
        python_inc = sysconfig.get_python_inc() # XXX refactor remaining dependencies
                                                # like obmalloc into separately compilable
                                                # modules etc.
        pypy_include_dir = py.path.local(autopath.pypydir).join('translator', 'c')
        include_dirs = [python_inc, pypy_include_dir]
        return ExternalCompilationInfo(include_dirs=include_dirs)

    def build_database(self):
        translator = self.translator

        gcpolicyclass = self.get_gcpolicyclass()

        if self.config.translation.gcrootfinder == "asmgcc":
            if not self.standalone:
                raise NotImplementedError("--gcrootfinder=asmgcc requires standalone")

        if self.config.translation.stackless:
            if not self.standalone:
                raise Exception("stackless: only for stand-alone builds")
            
            from pypy.translator.stackless.transform import StacklessTransformer
            stacklesstransformer = StacklessTransformer(
                translator, self.originalentrypoint,
                stackless_gc=gcpolicyclass.requires_stackless)
            self.entrypoint = stacklesstransformer.slp_entry_point
        else:
            stacklesstransformer = None

        db = LowLevelDatabase(translator, standalone=self.standalone,
                              gcpolicyclass=gcpolicyclass,
                              stacklesstransformer=stacklesstransformer,
                              thread_enabled=self.config.translation.thread,
                              sandbox=self.config.translation.sandbox)
        self.db = db
        
        # give the gc a chance to register interest in the start-up functions it
        # need (we call this for its side-effects of db.get())
        list(db.gcpolicy.gc_startup_code())

        # build entrypoint and eventually other things to expose
        pf = self.getentrypointptr()
        pfname = db.get(pf)
        self.c_entrypoint_name = pfname
        db.complete()

        self.collect_compilation_info(db)
        return db

    have___thread = None

    def collect_compilation_info(self, db):
        # we need a concrete gcpolicy to do this
        self.eci = self.eci.merge(db.gcpolicy.compilation_info())

        all = []
        for node in self.db.globalcontainers():
            eci = getattr(node, 'compilation_info', None)
            if eci:
                all.append(eci)
        self.eci = self.eci.merge(*all)

    def get_gcpolicyclass(self):
        if self.gcpolicy is None:
            name = self.config.translation.gctransformer
            if self.config.translation.gcrootfinder == "asmgcc":
                name = "%s+asmgcroot" % (name,)
            return gc.name_to_gcpolicy[name]
        return self.gcpolicy

    # use generate_source(defines=DEBUG_DEFINES) to force the #definition
    # of the macros that enable debugging assertions
    DEBUG_DEFINES = {'RPY_ASSERT': 1,
                     'RPY_LL_ASSERT': 1}

    def generate_graphs_for_llinterp(self, db=None):
        # prepare the graphs as when the source is generated, but without
        # actually generating the source.
        if db is None:
            db = self.build_database()
        graphs = db.all_graphs()
        db.gctransformer.prepare_inline_helpers(graphs)
        for node in db.containerlist:
            if isinstance(node, FuncNode):
                for funcgen in node.funcgens:
                    funcgen.patch_graph(copy_graph=False)
        return db

    def generate_source(self, db=None, defines={}):
        assert self.c_source_filename is None
        translator = self.translator

        if db is None:
            db = self.build_database()
        pf = self.getentrypointptr()
        pfname = db.get(pf)
        if self.modulename is None:
            self.modulename = uniquemodulename('testing')
        modulename = self.modulename
        targetdir = udir.ensure(modulename, dir=1)
        
        self.targetdir = targetdir
        defines = defines.copy()
        if self.config.translation.countmallocs:
            defines['COUNT_OP_MALLOCS'] = 1
        if self.config.translation.sandbox:
            defines['RPY_SANDBOXED'] = 1
        if CBuilder.have___thread is None:
            CBuilder.have___thread = self.translator.platform.check___thread()
        if not self.standalone:
            assert not self.config.translation.instrument
            self.eci, cfile, extra = gen_source(db, modulename, targetdir,
                                                self.eci,
                                                defines = defines)
        else:
            if self.config.translation.instrument:
                defines['INSTRUMENT'] = 1
            if CBuilder.have___thread:
                if not self.config.translation.no__thread:
                    defines['USE___THREAD'] = 1
            self.eci, cfile, extra = gen_source_standalone(db, modulename,
                                                 targetdir,
                                                 self.eci,
                                                 entrypointname = pfname,
                                                 defines = defines)
        self.c_source_filename = py.path.local(cfile)
        self.extrafiles = self.eventually_copy(extra)
        self.gen_makefile(targetdir)
        return cfile

    def eventually_copy(self, cfiles):
        extrafiles = []
        for fn in cfiles:
            fn = py.path.local(fn)
            if not fn.relto(udir):
                newname = self.targetdir.join(fn.basename)
                fn.copy(newname)
                fn = newname
            extrafiles.append(fn)
        return extrafiles

class ModuleWithCleanup(object):
    def __init__(self, mod):
        self.__dict__['mod'] = mod

    def __getattr__(self, name):
        mod = self.__dict__['mod']
        obj = getattr(mod, name)
        parentself = self
        if callable(obj) and getattr(obj, '__module__', None) == mod.__name__:
            # The module must be kept alive with the function.
            # This wrapper avoids creating a cycle.
            class Wrapper:
                def __init__(self, obj):
                    self.myself = parentself
                    self.func = obj
                def __call__(self, *args, **kwargs):
                    return self.func(*args, **kwargs)
            obj = Wrapper(obj)
        return obj

    def __setattr__(self, name, val):
        mod = self.__dict__['mod']
        setattr(mod, name, val)

    def __del__(self):
        import sys
        if sys.platform == "win32":
            from _ctypes import FreeLibrary as dlclose
        else:
            from _ctypes import dlclose
        # XXX fish fish fish
        mod = self.__dict__['mod']
        dlclose(mod._lib._handle)
        try:
            del sys.modules[mod.__name__]
        except KeyError:
            pass


class CExtModuleBuilder(CBuilder):
    standalone = False
    _module = None
    _wrapper = None

    def getentrypointptr(self): # xxx
        if self._wrapper is None:
            self._wrapper = new_wrapper(self.entrypoint, self.translator)
        return self._wrapper

    def compile(self):
        assert self.c_source_filename 
        assert not self._compiled
        export_symbols = [self.db.get(self.getentrypointptr()),
                          'RPython_StartupCode',
                          ]
        if self.config.translation.countmallocs:
            export_symbols.append('malloc_counters')
        extsymeci = ExternalCompilationInfo(export_symbols=export_symbols)
        self.eci = self.eci.merge(extsymeci)

        if sys.platform == 'win32':
            self.eci = self.eci.merge(ExternalCompilationInfo(
                library_dirs = [py.path.local(sys.exec_prefix).join('LIBs'),
                                py.path.local(sys.executable).dirpath(),
                                ],
                ))


        files = [self.c_source_filename] + self.extrafiles
        self.translator.platform.compile(files, self.eci, standalone=False)
        self._compiled = True

    def _make_wrapper_module(self):
        fname = 'wrap_' + self.c_source_filename.purebasename
        modfile = self.c_source_filename.new(purebasename=fname, ext=".py")

        entrypoint_ptr = self.getentrypointptr()
        wrapped_entrypoint_c_name = self.db.get(entrypoint_ptr)
        
        CODE = """
import ctypes

_lib = ctypes.PyDLL(r"%(so_name)s")

_entry_point = getattr(_lib, "%(c_entrypoint_name)s")
_entry_point.restype = ctypes.py_object
_entry_point.argtypes = %(nargs)d*(ctypes.py_object,)

def entrypoint(*args):
    return _entry_point(*args)

try:
    _malloc_counters = _lib.malloc_counters
except AttributeError:
    pass
else:
    _malloc_counters.restype = ctypes.py_object
    _malloc_counters.argtypes = 2*(ctypes.py_object,)

    def malloc_counters():
        return _malloc_counters(None, None)

_rpython_startup = _lib.RPython_StartupCode
_rpython_startup()
""" % {'so_name': self.c_source_filename.new(ext=self.translator.platform.so_ext),
       'c_entrypoint_name': wrapped_entrypoint_c_name,
       'nargs': len(lltype.typeOf(entrypoint_ptr).TO.ARGS)}
        modfile.write(CODE)
        self._module_path = modfile
       
    def _import_module(self, isolated=False):
        if self._module is not None:
            return self._module
        assert self._compiled
        assert not self._module
        self._make_wrapper_module()
        if not isolated:
            mod = ModuleWithCleanup(self._module_path.pyimport())
        else:
            mod = isolate.Isolate((str(self._module_path.dirpath()),
                                   self._module_path.purebasename))
        self._module = mod
        return mod
        
    def get_entry_point(self, isolated=False):
        self._import_module(isolated=isolated)
        return getattr(self._module, "entrypoint")

    def get_malloc_counters(self, isolated=False):
        self._import_module(isolated=isolated)
        return self._module.malloc_counters
                       
    def cleanup(self):
        #assert self._module
        if isinstance(self._module, isolate.Isolate):
            isolate.close_isolate(self._module)

    def gen_makefile(self, targetdir):
        pass

class CStandaloneBuilder(CBuilder):
    standalone = True
    executable_name = None

    def getprofbased(self):
        profbased = None
        if self.config.translation.instrumentctl is not None:
            profbased = self.config.translation.instrumentctl
        else:
            # xxx handling config.translation.profopt is a bit messy, because
            # it could be an empty string (not to be confused with None) and
            # because noprofopt can be used as an override.
            profopt = self.config.translation.profopt
            if profopt is not None and not self.config.translation.noprofopt:
                profbased = (ProfOpt, profopt)
        return profbased

    def has_profopt(self):
        profbased = self.getprofbased()
        return (profbased and isinstance(profbased, tuple)
                and profbased[0] is ProfOpt)

    def getentrypointptr(self):
        # XXX check that the entrypoint has the correct
        # signature:  list-of-strings -> int
        bk = self.translator.annotator.bookkeeper
        return getfunctionptr(bk.getdesc(self.entrypoint).getuniquegraph())

    def cmdexec(self, args=''):
        assert self._compiled
        res = self.translator.platform.execute(self.executable_name, args)
        if res.returncode != 0:
            raise Exception("Returned %d" % (res.returncode,))
        return res.out

    def compile(self):
        assert self.c_source_filename
        assert not self._compiled
        if self.config.translation.gcrootfinder == "asmgcc":
            self.translator.platform.execute_makefile(self.targetdir)
        else:
            compiler = CCompilerDriver(self.translator.platform,
                                       [self.c_source_filename] + self.extrafiles,
                                       self.eci, profbased=self.getprofbased())
            self.executable_name = compiler.build()
            assert self.executable_name
        self._compiled = True
        return self.executable_name

    def gen_makefile(self, targetdir):
        cfiles = [self.c_source_filename] + self.extrafiles
        mk = self.translator.platform.gen_makefile(cfiles, self.eci,
                                                   path=targetdir)
        if self.has_profopt():
            profopt = self.config.translation.profopt
            mk.definition('ABS_TARGET', '$(shell python -c "import sys,os; print os.path.abspath(sys.argv[1])" $(TARGET))')
            mk.definition('DEFAULT_TARGET', 'profopt')
            mk.definition('PROFOPT', profopt)

        rules = [
            ('clean', '', 'rm -f $(OBJECTS) $(TARGET) $(GCMAPFILES) *.gc?? ../module_cache/*.gc??'),
            ('clean_noprof', '', 'rm -f $(OBJECTS) $(TARGET) $(GCMAPFILES)'),
            ('debug', '', '$(MAKE) CFLAGS="-g -O1 -DRPY_ASSERT" $(TARGET)'),
            ('debug_exc', '', '$(MAKE) CFLAGS="-g -O1 -DRPY_ASSERT -DDO_LOG_EXC" $(TARGET)'),
            ('debug_mem', '', '$(MAKE) CFLAGS="-g -O1 -DRPY_ASSERT -DTRIVIAL_MALLOC_DEBUG" $(TARGET)'),
            ('no_obmalloc', '', '$(MAKE) CFLAGS="-g -O1 -DRPY_ASSERT -DNO_OBMALLOC" $(TARGET)'),
            ('linuxmemchk', '', '$(MAKE) CFLAGS="-g -O1 -DRPY_ASSERT -DLINUXMEMCHK" $(TARGET)'),
            ('llsafer', '', '$(MAKE) CFLAGS="-O2 -DRPY_LL_ASSERT" $(TARGET)'),
            ('lldebug', '', '$(MAKE) CFLAGS="-g -O1 -DRPY_ASSERT -DRPY_LL_ASSERT" $(TARGET)'),
            ('profile', '', '$(MAKE) CFLAGS="-g -O1 -pg $(CFLAGS)" LDFLAGS="-pg $(LDFLAGS)" $(TARGET)'),
            ]
        if self.has_profopt():
            rules.append(
                ('profopt', '', [
                '$(MAKENOPROF)',
                '$(MAKE) CFLAGS="-fprofile-generate $(CFLAGS)" LDFLAGS="-fprofile-generate $(LDFLAGS)" $(TARGET)',
                'cd $(PYPYDIR)/translator/goal && $(ABS_TARGET) $(PROFOPT)',
                '$(MAKE) clean_noprof',
                '$(MAKE) CFLAGS="-fprofile-use $(CFLAGS)" LDFLAGS="-fprofile-use $(LDFLAGS)" $(TARGET)']))
        for rule in rules:
            mk.rule(*rule)

        if self.config.translation.gcrootfinder == 'asmgcc':
            ofiles = ['%s.s' % (cfile[:-2],) for cfile in mk.cfiles]
            gcmapfiles = ['%s.gcmap' % (cfile[:-2],) for cfile in mk.cfiles]
            mk.definition('ASMFILES', ofiles)
            mk.definition('GCMAPFILES', gcmapfiles)
            mk.definition('OBJECTS', '$(ASMFILES) gcmaptable.s')
            mk.rule('%.s', '%.c', '$(CC) $(CFLAGS) -frandom-seed=$< -o $@ -S $< $(INCLUDEDIRS)')
            mk.rule('%.gcmap', '%.s', '$(PYPYDIR)/translator/c/gcc/trackgcroot.py -t $< > $@ || (rm -f $@ && exit 1)')
            mk.rule('gcmaptable.s', '$(GCMAPFILES)', '$(PYPYDIR)/translator/c/gcc/trackgcroot.py $(GCMAPFILES) > $@ || (rm -f $@ && exit 1)')

        mk.write()
        #self.translator.platform,
        #                           ,
        #                           self.eci, profbased=self.getprofbased()
        self.executable_name = mk.exe_name

# ____________________________________________________________

SPLIT_CRITERIA = 65535 # support VC++ 7.2
#SPLIT_CRITERIA = 32767 # enable to support VC++ 6.0

MARKER = '/*/*/' # provide an easy way to split after generating

class SourceGenerator:
    one_source_file = True

    def __init__(self, database, preimplementationlines=[]):
        self.database = database
        self.preimpl = preimplementationlines
        self.extrafiles = []
        self.path = None
        self.namespace = NameManager()

    def set_strategy(self, path):
        all_nodes = list(self.database.globalcontainers())
        # split off non-function nodes. We don't try to optimize these, yet.
        funcnodes = []
        othernodes = []
        for node in all_nodes:
            if node.nodekind == 'func':
                funcnodes.append(node)
            else:
                othernodes.append(node)
        # for now, only split for stand-alone programs.
        if self.database.standalone:
            self.one_source_file = False
        self.funcnodes = funcnodes
        self.othernodes = othernodes
        self.path = path

    def uniquecname(self, name):
        assert name.endswith('.c')
        return self.namespace.uniquename(name[:-2]) + '.c'

    def makefile(self, name):
        log.writing(name)
        filepath = self.path.join(name)
        if name.endswith('.c'):
            self.extrafiles.append(filepath)
        return filepath.open('w')

    def getextrafiles(self):
        return self.extrafiles

    def getothernodes(self):
        return self.othernodes[:]

    def splitnodesimpl(self, basecname, nodes, nextra, nbetween,
                       split_criteria=SPLIT_CRITERIA):
        # produce a sequence of nodes, grouped into files
        # which have no more than SPLIT_CRITERIA lines
        iternodes = iter(nodes)
        done = [False]
        def subiter():
            used = nextra
            for node in iternodes:
                impl = '\n'.join(list(node.implementation())).split('\n')
                if not impl:
                    continue
                cost = len(impl) + nbetween
                yield node, impl
                del impl
                if used + cost > split_criteria:
                    # split if criteria met, unless we would produce nothing.
                    raise StopIteration
                used += cost
            done[0] = True
        while not done[0]:
            yield self.uniquecname(basecname), subiter()

    def gen_readable_parts_of_source(self, f):
        if py.std.sys.platform != "win32":
            split_criteria_big = SPLIT_CRITERIA * 4 
        else:
            split_criteria_big = SPLIT_CRITERIA
        if self.one_source_file:
            return gen_readable_parts_of_main_c_file(f, self.database,
                                                     self.preimpl)
        #
        # All declarations
        #
        database = self.database
        structdeflist = database.getstructdeflist()
        name = 'structdef.h'
        fi = self.makefile(name)
        print >> f, '#include "%s"' % name
        gen_structdef(fi, database)
        fi.close()
        name = 'forwarddecl.h'
        fi = self.makefile(name)
        print >> f, '#include "%s"' % name
        gen_forwarddecl(fi, database)
        fi.close()

        #
        # Implementation of functions and global structures and arrays
        #
        print >> f
        print >> f, '/***********************************************************/'
        print >> f, '/***  Implementations                                    ***/'
        print >> f
        for line in self.preimpl:
            print >> f, line
        print >> f, '#include "src/g_include.h"'
        print >> f
        name = self.uniquecname('structimpl.c')
        print >> f, '/* %s */' % name
        fc = self.makefile(name)
        print >> fc, '/***********************************************************/'
        print >> fc, '/***  Structure Implementations                          ***/'
        print >> fc
        print >> fc, '#define PYPY_NOT_MAIN_FILE'
        print >> fc, '#include "common_header.h"'
        print >> fc, '#include "structdef.h"'
        print >> fc, '#include "forwarddecl.h"'
        print >> fc
        print >> fc, '#include "src/g_include.h"'
        print >> fc
        print >> fc, MARKER

        print >> fc, '/***********************************************************/'
        fc.close()

        nextralines = 11 + 1
        for name, nodeiter in self.splitnodesimpl('nonfuncnodes.c',
                                                   self.othernodes,
                                                   nextralines, 1):
            print >> f, '/* %s */' % name
            fc = self.makefile(name)
            print >> fc, '/***********************************************************/'
            print >> fc, '/***  Non-function Implementations                       ***/'
            print >> fc
            print >> fc, '#define PYPY_NOT_MAIN_FILE'
            print >> fc, '#include "common_header.h"'
            print >> fc, '#include "structdef.h"'
            print >> fc, '#include "forwarddecl.h"'
            print >> fc
            print >> fc, '#include "src/g_include.h"'
            print >> fc
            print >> fc, MARKER
            for node, impl in nodeiter:
                print >> fc, '\n'.join(impl)
                print >> fc, MARKER
            print >> fc, '/***********************************************************/'
            fc.close()

        nextralines = 8 + len(self.preimpl) + 4 + 1
        for name, nodeiter in self.splitnodesimpl('implement.c',
                                                   self.funcnodes,
                                                   nextralines, 1,
                                                   split_criteria_big):
            print >> f, '/* %s */' % name
            fc = self.makefile(name)
            print >> fc, '/***********************************************************/'
            print >> fc, '/***  Implementations                                    ***/'
            print >> fc
            print >> fc, '#define PYPY_NOT_MAIN_FILE'
            print >> fc, '#include "common_header.h"'
            print >> fc, '#include "structdef.h"'
            print >> fc, '#include "forwarddecl.h"'
            print >> fc
            for line in self.preimpl:
                print >> fc, line
            print >> fc
            print >> fc, '#include "src/g_include.h"'
            print >> fc
            print >> fc, MARKER
            for node, impl in nodeiter:
                print >> fc, '\n'.join(impl)
                print >> fc, MARKER
            print >> fc, '/***********************************************************/'
            fc.close()
        print >> f


def gen_structdef(f, database):
    structdeflist = database.getstructdeflist()
    print >> f, '/***********************************************************/'
    print >> f, '/***  Structure definitions                              ***/'
    print >> f
    for node in structdeflist:
        if hasattr(node, 'forward_decl'):
            if node.forward_decl:
                print >> f, node.forward_decl
        else:
            print >> f, '%s %s;' % (node.typetag, node.name)
    print >> f
    for node in structdeflist:
        for line in node.definition():
            print >> f, line

def gen_forwarddecl(f, database):
    print >> f, '/***********************************************************/'
    print >> f, '/***  Forward declarations                               ***/'
    print >> f
    for node in database.globalcontainers():
        for line in node.forward_declaration():
            print >> f, line

# this function acts as the fallback for small sources for now.
# Maybe we drop this completely if source splitting is the way
# to go. Currently, I'm quite fine with keeping a working fallback.
# XXX but we need to reduce code duplication.

def gen_readable_parts_of_main_c_file(f, database, preimplementationlines=[]):
    #
    # All declarations
    #
    print >> f
    gen_structdef(f, database)
    print >> f
    gen_forwarddecl(f, database)

    #
    # Implementation of functions and global structures and arrays
    #
    print >> f
    print >> f, '/***********************************************************/'
    print >> f, '/***  Implementations                                    ***/'
    print >> f
    for line in preimplementationlines:
        print >> f, line
    print >> f, '#include "src/g_include.h"'
    print >> f
    blank = True
    graphs = database.all_graphs()
    database.gctransformer.prepare_inline_helpers(graphs)
    for node in database.globalcontainers():
        if blank:
            print >> f
            blank = False
        for line in node.implementation():
            print >> f, line
            blank = True

def gen_startupcode(f, database):
    # generate the start-up code and put it into a function
    print >> f, 'char *RPython_StartupCode(void) {'
    print >> f, '\tchar *error = NULL;'
    for line in database.gcpolicy.gc_startup_code():
        print >> f,"\t" + line

    # put float infinities in global constants, we should not have so many of them for now to make
    # a table+loop preferable
    for dest, value in database.late_initializations:
        print >> f, "\t%s = %s;" % (dest, value)

    firsttime = True
    for node in database.containerlist:
        lines = list(node.startupcode())
        if lines:
            if firsttime:
                firsttime = False
            else:
                print >> f, '\tif (error) return error;'
            for line in lines:
                print >> f, '\t'+line
    print >> f, '\treturn error;'
    print >> f, '}'

def gen_source_standalone(database, modulename, targetdir, eci,
                          entrypointname, defines={}): 
    assert database.standalone
    if isinstance(targetdir, str):
        targetdir = py.path.local(targetdir)
    filename = targetdir.join(modulename + '.c')
    f = filename.open('w')
    incfilename = targetdir.join('common_header.h')
    fi = incfilename.open('w')

    #
    # Header
    #
    print >> f, '#include "common_header.h"'
    print >> f
    defines['PYPY_STANDALONE'] = entrypointname
    for key, value in defines.items():
        print >> fi, '#define %s %s' % (key, value)

    print >> fi, '#define Py_BUILD_CORE  /* for Windows: avoid pulling libs in */'
    print >> fi, '#include "pyconfig.h"'

    eci.write_c_header(fi)
    print >> fi, '#include "src/g_prerequisite.h"'

    fi.close()

    preimplementationlines = list(
        pre_include_code_lines(database, database.translator.rtyper))

    #
    # 1) All declarations
    # 2) Implementation of functions and global structures and arrays
    #
    sg = SourceGenerator(database, preimplementationlines)
    sg.set_strategy(targetdir)
    database.prepare_inline_helpers()
    sg.gen_readable_parts_of_source(f)

    # 3) start-up code
    print >> f
    gen_startupcode(f, database)

    f.close()

    if 'INSTRUMENT' in defines:
        fi = incfilename.open('a')
        n = database.instrument_ncounter
        print >>fi, "#define INSTRUMENT_NCOUNTER %d" % n
        fi.close()

    eci = eci.convert_sources_to_files(being_main=True)
    files, eci = eci.get_module_files()
    return eci, filename, sg.getextrafiles() + list(files)

def gen_source(database, modulename, targetdir, eci, defines={}):
    assert not database.standalone
    if isinstance(targetdir, str):
        targetdir = py.path.local(targetdir)
    filename = targetdir.join(modulename + '.c')
    f = filename.open('w')
    incfilename = targetdir.join('common_header.h')
    fi = incfilename.open('w')

    #
    # Header
    #
    print >> f, '#include "common_header.h"'
    print >> f
    for key, value in defines.items():
        print >> fi, '#define %s %s' % (key, value)

    print >> fi, '#include "pyconfig.h"'

    eci.write_c_header(fi)
    print >> fi, '#include "src/g_prerequisite.h"'

    fi.close()

    if database.translator is None or database.translator.rtyper is None:
        preimplementationlines = []
    else:
        preimplementationlines = list(
            pre_include_code_lines(database, database.translator.rtyper))

    #
    # 1) All declarations
    # 2) Implementation of functions and global structures and arrays
    #
    sg = SourceGenerator(database, preimplementationlines)
    sg.set_strategy(targetdir)
    sg.gen_readable_parts_of_source(f)

    gen_startupcode(f, database)
    f.close()

    eci = eci.convert_sources_to_files(being_main=True)
    files, eci = eci.get_module_files()
    return eci, filename, sg.getextrafiles() + list(files)
