# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'listobject_8f7e972c4aabc2fc7c8f6414d20ee41a')
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
## filename    'objspace/std/listobject.py'
## function    'listrepr'
## firstlineno 312
##SECTION##
# global declarations
# global object g4dict
# global object gs___name__
# global object gs___builtin__
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_listrepr
# global object gfunc_listrepr
# global object gs______
# global object gi_1
# global object gs_append
# global object gbltinmethod_join
# global object gs___
# global object gs_join
# global object gs__
# global object gs___1

  def listrepr(space, w_currently_in_repr, w_l):
    """The app-level part of repr()."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_list_id = space.id(w_l)
            w_0 = space.contains(w_currently_in_repr, w_list_id)
            v0 = space.is_true(w_0)
            if v0 == True:
                w_1 = gs______
                goto = 11
            else:
                goto = 2

        if goto == 2:
            w_2 = space.setitem(w_currently_in_repr, w_list_id, gi_1)
            w___1_ = space.newlist([])
            w_3 = space.iter(w_l)
            goto = 3

        if goto == 3:
            try:
                w_4 = space.next(w_3)
                goto = 4
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 6
                elif e.match(space, space.w_RuntimeError):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 4:
            try:
                w_5 = space.repr(w_4)
                goto = 5
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 5:
            try:
                w_6 = space.getattr(w___1_, gs_append)
                goto = 8
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 6:
            try:
                w_7 = space.call_function(gbltinmethod_join, w___1_)
                goto = 7
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 7:
            w_8 = space.add(gs__, w_7)
            w_9 = space.add(w_8, gs___1)
            try:
                w_10 = space.delitem(w_currently_in_repr, w_list_id)
                w_1 = w_9
                goto = 11
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_Exception):
                    w_1 = w_9
                    goto = 11
                else:raise # unhandled case, should not happen

        if goto == 8:
            try:
                w_11 = space.call_function(w_6, w_5)
                goto = 3
                continue
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 9:
            try:
                w_12 = space.delitem(w_currently_in_repr, w_list_id)
                goto = 10
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_Exception):
                    goto = 10
                else:raise # unhandled case, should not happen

        if goto == 10:
            raise gOperationError(w_etype, w_evalue)

        if goto == 11:
            return w_1

  fastf_listrepr = listrepr
  fastf_listrepr.__name__ = 'fastf_listrepr'

##SECTION##
  g4dict = space.newdict()
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g4dict, gs___name__, gs___builtin__)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/objspace/std/listobject.py""")
  space.setitem(g4dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_listrepr = space.new_interned_str('listrepr')
  from pypy.interpreter import gateway
  gfunc_listrepr = space.wrap(gateway.interp2app(fastf_listrepr, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g4dict, gs_listrepr, gfunc_listrepr)
  gs______ = space.new_interned_str('[...]')
  gi_1 = space.wrap(1)
  from pypy.interpreter.error import OperationError as gOperationError
  gs_append = space.new_interned_str('append')
  gs___ = space.new_interned_str(', ')
  gs_join = space.new_interned_str('join')
  gbltinmethod_join = space.getattr(gs___, gs_join)
  gs__ = space.new_interned_str('[')
  gs___1 = space.new_interned_str(']')
  return g4dict


from pypy._cache import known_code
known_code['8f7e972c4aabc2fc7c8f6414d20ee41a'] = init__builtin__
