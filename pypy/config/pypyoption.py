import autopath
import py, os
import sys
from pypy.config.config import OptionDescription, BoolOption, IntOption, ArbitraryOption
from pypy.config.config import ChoiceOption, StrOption, to_optparse, Config
from pypy.config.config import ConflictConfigError

modulepath = py.magic.autopath().dirpath().dirpath().join("module")
all_modules = [p.basename for p in modulepath.listdir()
               if p.check(dir=True, dotfile=False)
               and p.join('__init__.py').check()]

essential_modules = dict.fromkeys(
    ["exceptions", "_file", "sys", "__builtin__", "posix"]
)

default_modules = essential_modules.copy()
default_modules.update(dict.fromkeys(
    ["_codecs", "gc", "_weakref", "marshal", "errno",
     "math", "_sre", "_pickle_support", "operator",
     "recparser", "symbol", "_random", "__pypy__"]))


# --allworkingmodules
working_modules = default_modules.copy()
working_modules.update(dict.fromkeys(
    ["_socket", "unicodedata", "mmap", "fcntl",
      "rctime" , "select", "zipimport", "_lsprof",
     "crypt", "signal", "dyngram", "_rawffi", "termios", "zlib",
     "struct", "md5", "sha", "bz2", "_minimal_curses", "cStringIO",
     "thread", "itertools", "pyexpat", "_ssl"]
))

working_oo_modules = default_modules.copy()
working_oo_modules.update(dict.fromkeys(
    ["md5", "sha", "cStringIO", "itertools"]
))

# XXX this should move somewhere else, maybe to platform ("is this posixish"
#     check or something)
if sys.platform == "win32":
    working_modules["_winreg"] = None
    # unix only modules
    del working_modules["crypt"]
    del working_modules["fcntl"]
    del working_modules["termios"]
    del working_modules["_minimal_curses"]

    # The _locale module is probably incomplete,
    # but enough for the tests to pass on Windows
    working_modules["_locale"] = None

if sys.platform == "sunos5":
    del working_modules['mmap']   # depend on ctypes, can't get at c-level 'errono'
    del working_modules['rctime'] # depend on ctypes, missing tm_zone/tm_gmtoff
    del working_modules['signal'] # depend on ctypes, can't get at c-level 'errono'
    del working_modules['fcntl']  # LOCK_NB not defined
    del working_modules["_minimal_curses"]
    del working_modules["termios"]



module_dependencies = {}
module_suggests = {    # the reason you want _rawffi is for ctypes, which
                       # itself needs the interp-level struct module
                       # because 'P' is missing from the app-level one
                       '_rawffi': [("objspace.usemodules.struct", True)],
                       }

module_import_dependencies = {
    # no _rawffi if importing pypy.rlib.libffi raises ImportError
    # or CompilationError
    "_rawffi"   : ["pypy.rlib.libffi"],

    "zlib"      : ["pypy.rlib.rzlib"],
    "bz2"       : ["pypy.module.bz2.interp_bz2"],
    "pyexpat"   : ["pypy.module.pyexpat.interp_pyexpat"],
    "_ssl"      : ["pypy.module._ssl.interp_ssl"],
    }

def get_module_validator(modname):
    if modname in module_import_dependencies:
        modlist = module_import_dependencies[modname]
        def validator(config):
            from pypy.rpython.tool.rffi_platform import CompilationError
            try:
                for name in modlist:
                    __import__(name)
            except (ImportError, CompilationError), e:
                errcls = e.__class__.__name__
                config.add_warning(
                    "The module %r is disabled\n" % (modname,) +
                    "because importing %s raised %s\n" % (name, errcls) +
                    str(e))
                raise ConflictConfigError("--withmod-%s: %s" % (modname,
                                                                errcls))
        return validator
    else:
        return None


pypy_optiondescription = OptionDescription("objspace", "Object Space Options", [
    ChoiceOption("name", "Object Space name",
                 ["std", "flow", "thunk", "dump", "taint", "reflective"],
                 "std",
                 requires={"reflective":
                               [("objspace.disable_call_speedhacks", True)]
                          },
                 cmdline='--objspace -o'),

    ChoiceOption("parser", "which parser to use for app-level code",
                 ["pypy", "cpython"], "pypy",
                 cmdline='--parser'),

    ChoiceOption("compiler", "which compiler to use for app-level code",
                 ["cpython", "ast"], "ast",
                 cmdline='--compiler'),

    OptionDescription("opcodes", "opcodes to enable in the interpreter", [
        BoolOption("CALL_LIKELY_BUILTIN", "emit a special bytecode for likely calls to builtin functions",
                   default=False,
                   requires=[("objspace.std.withmultidict", True),
                             ("translation.stackless", False)]),
        BoolOption("CALL_METHOD", "emit a special bytecode for expr.name()",
                   default=False),
        ]),

    BoolOption("nofaking", "disallow faking in the object space",
               default=False,
               requires=[
                   ("objspace.usemodules.posix", True),
                   ("objspace.usemodules.time", True),
                   ("objspace.usemodules.errno", True)],
               cmdline='--nofaking'),

    OptionDescription("usemodules", "Which Modules should be used", [
        BoolOption(modname, "use module %s" % (modname, ),
                   default=modname in default_modules,
                   cmdline="--withmod-%s" % (modname, ),
                   requires=module_dependencies.get(modname, []),
                   suggests=module_suggests.get(modname, []),
                   negation=modname not in essential_modules,
                   validator=get_module_validator(modname))
        for modname in all_modules]),

    BoolOption("allworkingmodules", "use as many working modules as possible",
               # NB. defaults to True, but in py.py this is overridden by
               # a False suggestion because it takes a while to start up.
               # Actual module enabling only occurs if
               # enable_allworkingmodules() is called, and it depends
               # on the selected backend.
               default=True,
               cmdline="--allworkingmodules",
               negation=True),

    BoolOption("geninterp", "specify whether geninterp should be used",
               cmdline=None,
               default=True),

    BoolOption("logbytecodes",
               "keep track of bytecode usage",
               default=False),

    BoolOption("usepycfiles", "Write and read pyc files when importing",
               default=True),

    BoolOption("lonepycfiles", "Import pyc files with no matching py file",
               default=False,
               requires=[("objspace.usepycfiles", True)]),

    BoolOption("honor__builtins__",
               "Honor the __builtins__ key of a module dictionary",
               default=False),

    BoolOption("disable_call_speedhacks",
               "make sure that all calls go through space.call_args",
               default=False),

    BoolOption("timing",
               "timing of various parts of the interpreter (simple profiling)",
               default=False),

    OptionDescription("std", "Standard Object Space Options", [
        BoolOption("withtproxy", "support transparent proxies",
                   default=True),

        BoolOption("withsmallint", "use tagged integers",
                   default=False,
                   requires=[("translation.gc", "boehm"),
                             ("objspace.std.withprebuiltint", False)]),

        BoolOption("withprebuiltint", "prebuild commonly used int objects",
                   default=False),

        IntOption("prebuiltintfrom", "lowest integer which is prebuilt",
                  default=-5, cmdline="--prebuiltintfrom"),

        IntOption("prebuiltintto", "highest integer which is prebuilt",
                  default=100, cmdline="--prebuiltintto"),

        BoolOption("withstrjoin", "use strings optimized for addition",
                   default=False),

        BoolOption("withstrslice", "use strings optimized for slicing",
                   default=False),

        BoolOption("withprebuiltchar",
                   "use prebuilt single-character string objects",
                   default=False),

        BoolOption("sharesmallstr",
                   "always reuse the prebuilt string objects "
                   "(the empty string and potentially single-char strings)",
                   default=False),

        BoolOption("withrope", "use ropes as the string implementation",
                   default=False,
                   requires=[("objspace.std.withstrslice", False),
                             ("objspace.std.withstrjoin", False)],
                   suggests=[("objspace.std.withprebuiltchar", True),
                             ("objspace.std.sharesmallstr", True)]),

        BoolOption("withropeunicode", "use ropes for the unicode implementation",
                   default=False,
                   requires=[("objspace.std.withrope", True)]),

        BoolOption("withmultidict",
                   "use dictionaries optimized for flexibility",
                   default=False),

        BoolOption("withsharingdict",
                   "use dictionaries that share the keys part",
                   default=False,
                   requires=[("objspace.std.withmultidict", True)]),

        BoolOption("withdictmeasurement",
                   "create huge files with masses of information "
                   "about dictionaries",
                   default=False,
                   requires=[("objspace.std.withmultidict", True)]),

        BoolOption("withbucketdict",
                   "use dictionaries with chained hash tables "
                   "(default is open addressing)",
                   default=False,
                   requires=[("objspace.std.withmultidict", True)]),

        BoolOption("withsmalldicts",
                   "handle small dictionaries differently",
                   default=False,
                   requires=[("objspace.std.withmultidict", True)]),

        BoolOption("withrangelist",
                   "enable special range list implementation that does not "
                   "actually create the full list until the resulting "
                   "list is mutated",
                   default=False),

        BoolOption("withtypeversion",
                   "version type objects when changing them",
                   cmdline=None,
                   default=False,
                   # weakrefs needed, because of get_subclasses()
                   requires=[("translation.rweakref", True)]),

        BoolOption("withshadowtracking",
                   "track whether an instance attribute shadows a type"
                   " attribute",
                   default=False,
                   requires=[("objspace.std.withmultidict", True),
                             ("objspace.std.withtypeversion", True),
                             ("translation.rweakref", True)]),
        BoolOption("withmethodcache",
                   "try to cache method lookups",
                   default=False,
                   requires=[("objspace.std.withtypeversion", True),
                             ("translation.rweakref", True)]),
        BoolOption("withmethodcachecounter",
                   "try to cache methods and provide a counter in __pypy__. "
                   "for testing purposes only.",
                   default=False,
                   requires=[("objspace.std.withmethodcache", True)]),
        IntOption("methodcachesizeexp",
                  " 2 ** methodcachesizeexp is the size of the of the method cache ",
                  default=11),
        BoolOption("withmultilist",
                   "use lists optimized for flexibility",
                   default=False,
                   requires=[("objspace.std.withrangelist", False),
                             ("objspace.name", "std"),
                             ("objspace.std.withtproxy", False)]),
        BoolOption("withfastslice",
                   "make list slicing lazy",
                   default=False,
                   requires=[("objspace.std.withmultilist", True)]),
        BoolOption("withchunklist",
                   "introducing a new nesting level to slow down list operations",
                   default=False,
                   requires=[("objspace.std.withmultilist", True)]),
        BoolOption("withsmartresizablelist",
                   "only overallocate O(sqrt(n)) elements for lists",
                   default=False,
                   requires=[("objspace.std.withmultilist", True)]),
        BoolOption("withblist",
                   "good asymptotic performance for very large lists",
                   default=False,
                   requires=[("objspace.std.withmultilist", True)]),
        BoolOption("optimized_int_add",
                   "special case the addition of two integers in BINARY_ADD",
                   default=False),
        BoolOption("optimized_comparison_op",
                   "special case the comparison of integers",
                   default=False),
        BoolOption("optimized_list_getitem",
                   "special case the 'list[integer]' expressions",
                   default=False),
        BoolOption("builtinshortcut",
                   "a shortcut for operations between built-in types",
                   default=False),
        BoolOption("getattributeshortcut",
                   "track types that override __getattribute__",
                   default=False),

        BoolOption("logspaceoptypes",
                   "a instrumentation option: before exit, print the types seen by "
                   "certain simpler bytecodes",
                   default=False),
        ChoiceOption("multimethods", "the multimethod implementation to use",
                     ["doubledispatch", "mrd"],
                     default="mrd"),
        BoolOption("immutable_builtintypes",
                   "Forbid the changing of builtin types", default=True),
     ]),
])

def get_pypy_config(overrides=None, translating=False):
    from pypy.config.translationoption import get_combined_translation_config
    return get_combined_translation_config(
            pypy_optiondescription, overrides=overrides,
            translating=translating)

def set_pypy_opt_level(config, level):
    """Apply PyPy-specific optimization suggestions on the 'config'.
    The optimizations depend on the selected level and possibly on the backend.
    """
    # warning: during some tests, the type_system and the backend may be
    # unspecified and we get None.  It shouldn't occur in translate.py though.
    type_system = config.translation.type_system
    backend = config.translation.backend

    # all the good optimizations for PyPy should be listed here
    if level in ['2', '3']:
        config.objspace.opcodes.suggest(CALL_LIKELY_BUILTIN=True)
        config.objspace.opcodes.suggest(CALL_METHOD=True)
        config.objspace.std.suggest(withmultidict=True)
        config.objspace.std.suggest(withshadowtracking=True)
        config.objspace.std.suggest(withrangelist=True)
        config.objspace.std.suggest(withmethodcache=True)
        config.objspace.std.suggest(withprebuiltchar=True)
        config.objspace.std.suggest(builtinshortcut=True)
        config.objspace.std.suggest(optimized_list_getitem=True)
        config.objspace.std.suggest(getattributeshortcut=True)

    # extra costly optimizations only go in level 3
    if level == '3':
        config.translation.suggest(profopt=
            "-c 'from richards import main;main(); "
                "from test import pystone; pystone.main()'")

    # memory-saving optimizations
    if level == 'mem':
        config.objspace.std.suggest(withprebuiltint=True)
        config.objspace.std.suggest(withrangelist=True)
        config.objspace.std.suggest(withprebuiltchar=True)
        config.objspace.std.suggest(withsharingdict=True)
        config.objspace.std.suggest(withstrslice=True)
        config.objspace.std.suggest(withstrjoin=True)
        # xxx other options? ropes maybe?

    # completely disable geninterp in a level 0 translation
    if level == '0':
        config.objspace.suggest(geninterp=False)

    # some optimizations have different effects depending on the typesystem
    if type_system == 'ootype':
        config.objspace.std.suggest(multimethods="doubledispatch")


def enable_allworkingmodules(config):
    if config.translation.type_system == 'ootype':
        modules = working_oo_modules
    else:
        modules = working_modules
    if config.translation.sandbox:
        modules = default_modules
    # ignore names from 'essential_modules', notably 'exceptions', which
    # may not be present in config.objspace.usemodules at all
    modules = [name for name in modules if name not in essential_modules]
    config.objspace.usemodules.suggest(**dict.fromkeys(modules, True))


if __name__ == '__main__':
    config = get_pypy_config()
    print config.getpaths()
    parser = to_optparse(config) #, useoptions=["translation.*"])
    option, args = parser.parse_args()
    print config
