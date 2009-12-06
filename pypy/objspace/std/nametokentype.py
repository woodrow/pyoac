from pypy.interpreter.error import OperationError
from pypy.objspace.descroperation import Object
from pypy.interpreter import gateway
from pypy.interpreter.typedef import default_identity_hash
from pypy.objspace.std.stdtypedef import *
from pypy.objspace.std.register_all import register_all
from pypy.objspace.std.objspace import StdObjSpace


def descr__repr__(space, w_obj):
    w = space.wrap
    w_type = space.type(w_obj)
    classname = w_type.getname(space, '?')
    w_module = w_type.lookup("__module__")
    if w_module is not None:
        try:
            modulename = space.str_w(w_module)
        except OperationError, e:
            if not e.match(space, space.w_TypeError):
                raise
        else:
            classname = '%s.%s' % (modulename, classname)
    return w_obj.getrepr(space, '%s object' % (classname,))

def descr__str__(space, w_obj):
    return space.repr(w_obj)

def descr__class__(space, w_obj):
    return space.type(w_obj)

def descr_set___class__(space, w_obj, w_newcls):
    from pypy.objspace.std.typeobject import W_TypeObject
    if not isinstance(w_newcls, W_TypeObject):
        raise OperationError(space.w_TypeError,
                             space.wrap("__class__ must be set to new-style class, not '%s' object" % 
                                        space.type(w_newcls).getname(space, '?')))
    if not w_newcls.is_heaptype():
        raise OperationError(space.w_TypeError,
                             space.wrap("__class__ assignment: only for heap types"))
    w_oldcls = space.type(w_obj)
    # XXX taint space should raise a TaintError here if w_oldcls is tainted
    assert isinstance(w_oldcls, W_TypeObject)
    if w_oldcls.get_full_instance_layout() == w_newcls.get_full_instance_layout():
        w_obj.setclass(space, w_newcls)
    else:
        raise OperationError(space.w_TypeError,
                             space.wrap("__class__ assignment: '%s' object layout differs from '%s'" %
                                        (w_oldcls.getname(space, '?'), w_newcls.getname(space, '?'))))
    

def descr__new__(space, w_type, __args__):
    from pypy.objspace.std.nametokenobject import W_NametokenObject
    from pypy.objspace.std.typetype import _precheck_for_new
    # don't allow arguments if the default object.__init__() is about
    # to be called
    w_type = _precheck_for_new(space, w_type)
    w_parentinit, w_ignored = w_type.lookup_where('__init__')
    if w_parentinit is space.w_object:
        try:
            __args__.fixedunpack(0)
        except ValueError:
            raise OperationError(space.w_TypeError,
                                 space.wrap("default __new__ takes "
                                            "no parameters"))
    w_obj = space.allocate_instance(W_NametokenObject, w_type)
    #W_ObjectObject.__init__(w_obj)
    return w_obj

def descr__init__(space, w_obj, __args__):
    pass

# ____________________________________________________________

nametoken_typedef = StdTypeDef("nametoken",
    __str__ = gateway.interp2app(descr__str__),
    __repr__ = gateway.interp2app(descr__repr__),
    __doc__ = '''Namespace capability token''',
    __new__ = newmethod(descr__new__,
                        unwrap_spec = [gateway.ObjSpace,gateway.W_Root,gateway.Arguments]),
    __hash__ = gateway.interp2app(default_identity_hash),
    __init__ = gateway.interp2app(descr__init__,
                                  unwrap_spec=[gateway.ObjSpace,gateway.W_Root,gateway.Arguments]),
    )
#    __class__ = GetSetProperty(descr__class__, descr_set___class__),

nametoken_typedef.custom_hash = False    # object.__hash__ is not a custom hash
nametoken_typedef.acceptable_as_base_class = False