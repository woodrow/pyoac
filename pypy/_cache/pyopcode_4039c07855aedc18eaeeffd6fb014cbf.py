# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'pyopcode_4039c07855aedc18eaeeffd6fb014cbf')
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
## function    'find_metaclass'
## firstlineno 1309
##SECTION##
# global declarations
# global object g4dict
# global object gs___name__
# global object gs___builtin__
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_find_metaclass
# global object gfunc_find_metaclass
# global object gs___metaclass__
# global object gi_0
# global object gs_hasattr
# global object gs___class__

  def find_metaclass(space, w_2, w_1, w_3, w_builtin):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.contains(w_1, gs___metaclass__)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_4 = space.getitem(w_1, gs___metaclass__)
            w_5 = w_4
            goto = 10

        if goto == 3:
            w_6 = space.len(w_2)
            w_7 = space.gt(w_6, gi_0)
            v1 = space.is_true(w_7)
            if v1 == True:
                goto = 4
            else:
                goto = 7

        if goto == 4:
            w_8 = space.getitem(w_2, gi_0)
            w_9 = space.call_function((space.builtin.get(space.str_w(gs_hasattr))), w_8, gs___class__)
            v2 = space.is_true(w_9)
            if v2 == True:
                goto = 5
            else:
                goto = 6

        if goto == 5:
            w_10 = space.getattr(w_8, gs___class__)
            w_5 = w_10
            goto = 10

        if goto == 6:
            w_11 = space.type(w_8)
            w_5 = w_11
            goto = 10

        if goto == 7:
            w_12 = space.contains(w_3, gs___metaclass__)
            v3 = space.is_true(w_12)
            if v3 == True:
                goto = 8
            else:
                goto = 9

        if goto == 8:
            w_13 = space.getitem(w_3, gs___metaclass__)
            w_5 = w_13
            goto = 10

        if goto == 9:
            try:
                w_14 = space.getattr(w_builtin, gs___metaclass__)
                w_5 = w_14
                goto = 10
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    w_5 = space.w_type
                    goto = 10
                else:raise # unhandled case, should not happen

        if goto == 10:
            return w_5

  fastf_find_metaclass = find_metaclass
  fastf_find_metaclass.__name__ = 'fastf_find_metaclass'

##SECTION##
  g4dict = space.newdict()
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g4dict, gs___name__, gs___builtin__)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/interpreter/pyopcode.py""")
  space.setitem(g4dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_find_metaclass = space.new_interned_str('find_metaclass')
  from pypy.interpreter import gateway
  gfunc_find_metaclass = space.wrap(gateway.interp2app(fastf_find_metaclass, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root, gateway.W_Root, gateway.W_Root]))
  space.setitem(g4dict, gs_find_metaclass, gfunc_find_metaclass)
  gs___metaclass__ = space.new_interned_str('__metaclass__')
  gi_0 = space.wrap(0)
  gs_hasattr = space.new_interned_str('hasattr')
  gs___class__ = space.new_interned_str('__class__')
  from pypy.interpreter.error import OperationError as gOperationError
  return g4dict


from pypy._cache import known_code
known_code['4039c07855aedc18eaeeffd6fb014cbf'] = init__builtin__
