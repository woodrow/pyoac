# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'pyopcode_85bad43c1b652dafe97b3ab4412af822')
    for ending in ('.py', '.pyc', '.pyo'):
        try:
            os.unlink(namestart+ending)
        except os.error:
            pass

#!/bin/env python
# -*- coding: LATIN-1 -*-

#*************************************************************
__name__ = "_geninterp_"+'__builtin__'
_geninterp_ = True

def init__builtin__(space):
  """NOT_RPYTHON"""

##SECTION##
## filename    'interpreter/pyopcode.py'
## function    'import_all_from'
## firstlineno 1330
##SECTION##
# global declarations
# global object g4dict
# global object gs___name__
# global object gs___builtin__
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_import_all_from
# global object gfunc_import_all_from
# global object gs___all__
# global object gs___dict__
# global object gs_from_import___object_has_no___di
# global object gs_keys
# global object gi_0
# global object gs__

  def import_all_from(space, w_module, w_into_locals):
    goto = 1 # startblock
    while True:

        if goto == 1:
            try:
                w_0 = space.getattr(w_module, gs___all__)
                w_skip_leading_underscores, w_1 = space.w_False, w_0
                goto = 7
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 2
                else:raise # unhandled case, should not happen

        if goto == 2:
            try:
                w_2 = space.getattr(w_module, gs___dict__)
                goto = 5
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 3
                else:raise # unhandled case, should not happen

        if goto == 3:
            w_3 = space.call_function(space.w_ImportError, gs_from_import___object_has_no___di)
            w_4 = space.type(w_3)
            w_5 = space.issubtype(w_4, space.w_type)
            v0 = space.is_true(w_5)
            if v0 == True:
                goto = 4
            else:
                goto = 6

        if goto == 4:
            w_6 = space.call_function(w_3, )
            w_7 = space.type(w_6)
            w_etype, w_evalue = w_7, w_6
            goto = 12

        if goto == 5:
            w_8 = space.getattr(w_2, gs_keys)
            w_9 = space.call_function(w_8, )
            w_skip_leading_underscores, w_1 = space.w_True, w_9
            goto = 7

        if goto == 6:
            w_10 = space.type(w_3)
            w_etype, w_evalue = w_10, w_3
            goto = 12

        if goto == 7:
            w_11 = space.iter(w_1)
            goto = 8

        if goto == 8:
            try:
                w_name = space.next(w_11)
                goto = 9
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_12 = space.w_None
                    goto = 13
                else:raise # unhandled case, should not happen

        if goto == 9:
            v1 = space.is_true(w_skip_leading_underscores)
            if v1 == True:
                goto = 10
            else:
                goto = 11

        if goto == 10:
            w_13 = space.getitem(w_name, gi_0)
            w_14 = space.eq(w_13, gs__)
            v2 = space.is_true(w_14)
            if v2 == True:
                goto = 8
                continue
            else:
                goto = 11

        if goto == 11:
            w_15 = space.getattr(w_module, w_name)
            w_16 = space.setitem(w_into_locals, w_name, w_15)
            goto = 8
            continue

        if goto == 12:
            raise gOperationError(w_etype, w_evalue)

        if goto == 13:
            return w_12

  fastf_import_all_from = import_all_from
  fastf_import_all_from.__name__ = 'fastf_import_all_from'

##SECTION##
  g4dict = space.newdict()
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g4dict, gs___name__, gs___builtin__)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/interpreter/pyopcode.py""")
  space.setitem(g4dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_import_all_from = space.new_interned_str('import_all_from')
  from pypy.interpreter import gateway
  gfunc_import_all_from = space.wrap(gateway.interp2app(fastf_import_all_from, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g4dict, gs_import_all_from, gfunc_import_all_from)
  gs___all__ = space.new_interned_str('__all__')
  from pypy.interpreter.error import OperationError as gOperationError
  gs___dict__ = space.new_interned_str('__dict__')
  gs_from_import___object_has_no___di = space.new_interned_str(
"""from-import-* object has no __dict__ and no __all__""")
  gs_keys = space.new_interned_str('keys')
  gi_0 = space.wrap(0)
  gs__ = space.new_interned_str('_')
  return g4dict


from pypy._cache import known_code
known_code['85bad43c1b652dafe97b3ab4412af822'] = init__builtin__
