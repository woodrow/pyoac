import pypy
from pypy.jit.metainterp.policy import ManualJitPolicy

from pypy.translator.backendopt.support import find_calls_from

class PyPyJitPolicy(ManualJitPolicy):

    def look_inside_function(self, func):
        mod = func.__module__ or '?'
        if func.__name__.startswith('__mm_'):
            return True
        if mod.startswith('pypy.objspace.'):
            return False
        if '_geninterp_' in func.func_globals: # skip all geninterped stuff
            return False
        if mod.startswith('pypy.interpreter.astcompiler.'):
            return False
        if mod.startswith('pypy.interpreter.pyparser.'):
            return False
        if mod.startswith('pypy.module.'):
            if not mod.startswith('pypy.module.pypyjit.'):
                return False
        if mod.startswith('pypy.translator.'):
            return False
        if mod in forbidden_modules:
            return False
        if func.__name__.startswith('_mm_') or '_mth_mm_' in func.__name__:
            return False
        if func.__name__.startswith('fastfunc_'):
            return False
        return super(PyPyJitPolicy, self).look_inside_function(func)

    def seebinary(self, opname):
        name2 = name1 = opname[:3].lower()
        if name1 in ('and', 'or'):
            name1 += '_'
        descr_impl = getattr(
                pypy.objspace.descroperation.DescrOperation, name1)
        obj_impl = getattr(pypy.objspace.std.intobject, name2 + '__Int_Int')
        self.seepath(
            getattr(pypy.interpreter.pyframe.PyFrame, 'BINARY_'+ opname),
            descr_impl,
            obj_impl)
        self.seepath(descr_impl,
                     pypy.objspace.std.typeobject.W_TypeObject.is_heaptype)
        descr_impl = getattr(pypy.objspace.descroperation.DescrOperation,
                             'inplace_' + name2)
        op_impl = getattr(pypy.interpreter.pyframe.PyFrame, 'INPLACE_'+ opname)
        self.seepath(op_impl, descr_impl, obj_impl)
        self.seepath(descr_impl,
                     pypy.objspace.std.typeobject.W_TypeObject.is_heaptype)
        
    def seeunary(self, opname, name=None):
        if name is None:
            name = opname.lower()
        descr_impl = getattr(
                pypy.objspace.descroperation.DescrOperation, name)
        self.seepath(
                getattr(pypy.interpreter.pyframe.PyFrame, 'UNARY_' + opname),
                descr_impl,
                getattr(pypy.objspace.std.intobject, name + '__Int'))
        self.seepath(descr_impl,
                pypy.objspace.std.typeobject.W_TypeObject.is_heaptype)

    def seecmp(self, name):
        descr_impl = getattr(pypy.objspace.descroperation.DescrOperation, name)
        self.seepath(
                pypy.interpreter.pyframe.PyFrame.COMPARE_OP,
                descr_impl,
                getattr(pypy.objspace.std.intobject, name +'__Int_Int'),
                pypy.objspace.std.Space.newbool)
        self.seepath(
                descr_impl,
                pypy.objspace.std.typeobject.W_TypeObject.is_heaptype)

    def fill_seen_graphs(self):
        import pypy
        def fc(o):
            return [i[1] for i in find_calls_from(self.translator, o)]


        # --------------------
        for binop in 'MODULO ADD SUBTRACT MULTIPLY AND OR XOR'.split():
            self.seebinary(binop)
        for cmpname in 'lt le eq ne ge gt'.split():
            self.seecmp(cmpname)
        self.seepath(pypy.interpreter.pyframe.PyFrame.UNARY_NOT,
                     pypy.objspace.std.Space.not_)
        self.seeunary('INVERT')
        self.seeunary('POSITIVE', 'pos')
        self.seeunary('NEGATIVE', 'neg')

        self.seepath(pypy.objspace.descroperation._invoke_binop,
                     pypy.objspace.descroperation._check_notimplemented)
        self.seepath(pypy.objspace.std.intobject.add__Int_Int,
                     pypy.objspace.std.inttype.wrapint,
                     pypy.objspace.std.intobject.W_IntObject.__init__)
        self.seepath(pypy.objspace.descroperation.DescrOperation.add,
                     pypy.objspace.std.Space.type,
                     pypy.objspace.std.Space.gettypeobject)
        self.seepath(pypy.objspace.descroperation.DescrOperation.add,
                     pypy.objspace.std.Space.is_w)
        self.seegraph(pypy.interpreter.pyframe.PyFrame.execute_frame, False)
        self.seegraph(pypy.objspace.std.multimethod.FailedToImplement.__init__,
                      True)
        # --------------------
        self.seepath(pypy.interpreter.pyframe.PyFrame.JUMP_IF_TRUE,
                     pypy.objspace.std.boolobject.nonzero__Bool)
        self.seepath(pypy.interpreter.pyframe.PyFrame.JUMP_IF_FALSE,
                     pypy.objspace.std.boolobject.nonzero__Bool)
        self.seepath(pypy.interpreter.pyframe.PyFrame.JUMP_IF_TRUE,
                     pypy.objspace.std.intobject.nonzero__Int)
        self.seepath(pypy.interpreter.pyframe.PyFrame.JUMP_IF_FALSE,
                     pypy.objspace.std.intobject.nonzero__Int)
        self.seepath(pypy.interpreter.pyframe.PyFrame.FOR_ITER,
                     pypy.objspace.descroperation.DescrOperation.next,
                     pypy.objspace.std.rangeobject.next__RangeIter,
                     pypy.objspace.std.rangeobject.W_RangeListObject.getitem)
        #
        #self.seepath(pypy.interpreter.pyframe.PyFrame.CALL_FUNCTION,
        #             pypy.interpreter.function.Function.funccall_valuestack)
        #self.seepath(pypy.interpreter.pyframe.PyFrame.CALL_FUNCTION,
        #             pypy.interpreter.function.Function.funccall_obj_valuestack)



forbidden_modules = {'pypy.interpreter.gateway': True,
                     #'pypy.interpreter.baseobjspace': True,
                     'pypy.interpreter.typedef': True,
                     'pypy.interpreter.eval': True,
                     'pypy.interpreter.function': True,
                     'pypy.interpreter.pytraceback': True,
                     }
