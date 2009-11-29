# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'dicttype_f5758cf4dec8f3b09eefeff37088fe7e')
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
## filename    'objspace/std/dicttype.py'
## function    'update1'
## firstlineno 66
##SECTION##
# global declarations
# global object gs_hasattr
# global object gdescriptor_dict___setitem__
# global object gs___setitem__
# global object gi_2

  def update1(space, w_d, w_1):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function((space.builtin.get(space.str_w(gs_hasattr))), w_1, gs_keys)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 7

        if goto == 2:
            w_2 = space.getattr(w_1, gs_keys)
            w_3 = space.call_function(w_2, )
            w_4 = space.iter(w_3)
            goto = 5

        if goto == 3:
            w_5 = space.getitem(w_6, gi_0)
            w_7 = space.getitem(w_6, gi_1)
            w_8 = space.call_function(gdescriptor_dict___setitem__, w_d, w_5, w_7)
            goto = 8

        if goto == 4:
            w_evalue = space.call_function(space.w_ValueError, )
            w_etype = space.type(w_evalue)
            goto = 10

        if goto == 5:
            try:
                w_10 = space.next(w_4)
                goto = 6
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_11 = space.w_None
                    goto = 11
                else:raise # unhandled case, should not happen

        if goto == 6:
            w_12 = space.getitem(w_1, w_10)
            w_13 = space.call_function(gdescriptor_dict___setitem__, w_d, w_10, w_12)
            goto = 5
            continue

        if goto == 7:
            w_9 = space.iter(w_1)
            goto = 8

        if goto == 8:
            try:
                w_6 = space.next(w_9)
                goto = 9
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_11 = space.w_None
                    goto = 11
                else:raise # unhandled case, should not happen

        if goto == 9:
            w_14 = space.len(w_6)
            w_15 = space.eq(w_14, gi_2)
            v1 = space.is_true(w_15)
            if v1 == True:
                goto = 3
                continue
            else:
                goto = 4
                continue

        if goto == 10:
            raise gOperationError(w_etype, w_evalue)

        if goto == 11:
            return w_11

  fastf_update1 = update1
  fastf_update1.__name__ = 'fastf_update1'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'update'
## firstlineno 74
##SECTION##
# global declaration
# global object gs_update_takes_at_most_1__non_keyw

  def update(space, __args__):
    funcname = "update"
    signature = ['d'], 'args', 'kwargs'
    defaults_w = []
    w_d, w_1, w_kwargs = __args__.parse(funcname, signature, defaults_w)
    return fastf_update(space, w_d, w_1, w_kwargs)

  f_update = update
  f_update.__name__ = 'f_update'

  def update(space, w_d, w_1, w_kwargs):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_1)
            w_2 = space.eq(w_0, gi_1)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_3 = space.getitem(w_1, gi_0)
            w_4 = fastf_update1(space, w_d, w_3)
            goto = 6

        if goto == 3:
            w_5 = space.gt(w_0, gi_1)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 4
            else:
                goto = 6

        if goto == 4:
            w_6 = space.call_function(space.w_TypeError, gs_update_takes_at_most_1__non_keyw)
            w_7 = space.type(w_6)
            w_8 = space.issubtype(w_7, space.w_type)
            v2 = space.is_true(w_8)
            if v2 == True:
                goto = 5
            else:
                goto = 8

        if goto == 5:
            w_9 = space.call_function(w_6, )
            w_10 = space.type(w_9)
            w_etype, w_evalue = w_10, w_9
            goto = 9

        if goto == 6:
            v3 = space.is_true(w_kwargs)
            if v3 == True:
                goto = 7
            else:
                w_11 = space.w_None
                goto = 10

        if goto == 7:
            w_12 = fastf_update1(space, w_d, w_kwargs)
            w_11 = space.w_None
            goto = 10

        if goto == 8:
            w_13 = space.type(w_6)
            w_etype, w_evalue = w_13, w_6
            goto = 9

        if goto == 9:
            raise gOperationError(w_etype, w_evalue)

        if goto == 10:
            return w_11

  fastf_update = update
  fastf_update.__name__ = 'fastf_update'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'popitem'
## firstlineno 83
##SECTION##
# global declarations
# global object gdescriptor_dict_iterkeys
# global object gs_popitem____dictionary_is_empty
# global object gdescriptor_dict___getitem__
# global object gs___getitem__
# global object gdescriptor_dict___delitem__
# global object gs___delitem__

  def popitem(space, w_d):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function(gdescriptor_dict_iterkeys, w_d)
            w_1 = space.iter(w_0)
            try:
                w_k = space.next(w_1)
                goto = 4
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 2
                else:raise # unhandled case, should not happen

        if goto == 2:
            w_2 = space.call_function(space.w_KeyError, gs_popitem____dictionary_is_empty)
            w_3 = space.type(w_2)
            w_4 = space.issubtype(w_3, space.w_type)
            v0 = space.is_true(w_4)
            if v0 == True:
                goto = 3
            else:
                goto = 5

        if goto == 3:
            w_5 = space.call_function(w_2, )
            w_6 = space.type(w_5)
            w_etype, w_evalue = w_6, w_5
            goto = 6

        if goto == 4:
            w_7 = space.call_function(gdescriptor_dict___getitem__, w_d, w_k)
            w_8 = space.call_function(gdescriptor_dict___delitem__, w_d, w_k)
            w_9 = space.newtuple([w_k, w_7])
            goto = 7

        if goto == 5:
            w_10 = space.type(w_2)
            w_etype, w_evalue = w_10, w_2
            goto = 6

        if goto == 6:
            raise gOperationError(w_etype, w_evalue)

        if goto == 7:
            return w_9

  fastf_popitem = popitem
  fastf_popitem.__name__ = 'fastf_popitem'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'get'
## firstlineno 92
##SECTION##
  def get(space, __args__):
    funcname = "get"
    signature = ['d', 'k', 'v'], None, None
    defaults_w = [space.w_None]
    w_1, w_2, w_v = __args__.parse(funcname, signature, defaults_w)
    return fastf_get(space, w_1, w_2, w_v)

  f_get = get
  f_get.__name__ = 'f_get'

  def get(space, w_1, w_2, w_v):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.contains(w_1, w_2)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                w_3 = w_v
                goto = 3

        if goto == 2:
            w_4 = space.call_function(gdescriptor_dict___getitem__, w_1, w_2)
            w_3 = w_4
            goto = 3

        if goto == 3:
            return w_3

  fastf_get = get
  fastf_get.__name__ = 'fastf_get'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'setdefault'
## firstlineno 98
##SECTION##
  def setdefault(space, __args__):
    funcname = "setdefault"
    signature = ['d', 'k', 'v'], None, None
    defaults_w = [space.w_None]
    w_1, w_2, w_v = __args__.parse(funcname, signature, defaults_w)
    return fastf_setdefault(space, w_1, w_2, w_v)

  f_setdefault = setdefault
  f_setdefault.__name__ = 'f_setdefault'

  def setdefault(space, w_1, w_2, w_v):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.contains(w_1, w_2)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_3 = space.call_function(gdescriptor_dict___getitem__, w_1, w_2)
            w_4 = w_3
            goto = 4

        if goto == 3:
            w_5 = space.call_function(gdescriptor_dict___setitem__, w_1, w_2, w_v)
            w_4 = w_v
            goto = 4

        if goto == 4:
            return w_4

  fastf_setdefault = setdefault
  fastf_setdefault.__name__ = 'fastf_setdefault'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'pop'
## firstlineno 105
##SECTION##
# global declarations
# global object gi_1
# global object gs_pop_expected_at_most_2_arguments
# global object gi_0

  def pop(space, w_d, w_k, w_defaults):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_defaults)
            w_1 = space.gt(w_0, gi_1)
            v0 = space.is_true(w_1)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_2 = space.len(w_defaults)
            w_3 = space.add(gi_1, w_2)
            w_4 = space.mod(gs_pop_expected_at_most_2_arguments, w_3)
            w_5 = space.is_(w_4, space.w_None)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 7
            else:
                goto = 9

        if goto == 3:
            try:
                w_v = space.call_function(gdescriptor_dict___getitem__, w_d, w_k)
                goto = 4
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_KeyError):
                    w_6 = e.w_value
                    goto = 5
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 13
                else:raise # unhandled case, should not happen

        if goto == 4:
            try:
                w_7 = space.call_function(gdescriptor_dict___delitem__, w_d, w_k)
                w_8 = w_v
                goto = 14
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_KeyError):
                    w_6 = e.w_value
                    goto = 5
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 13
                else:raise # unhandled case, should not happen

        if goto == 5:
            v2 = space.is_true(w_defaults)
            if v2 == True:
                goto = 6
            else:
                goto = 12

        if goto == 6:
            w_9 = space.getitem(w_defaults, gi_0)
            w_8 = w_9
            goto = 14

        if goto == 7:
            w_10 = space.call_function(space.w_TypeError, )
            w_11 = space.type(w_10)
            w_etype, w_evalue = w_11, w_10
            goto = 13

        if goto == 8:
            w_12 = space.type(w_6)
            w_etype, w_evalue = w_12, w_6
            goto = 13

        if goto == 9:
            w_13 = space.type(w_4)
            w_14 = space.issubtype(w_13, space.w_TypeError)
            v3 = space.is_true(w_14)
            if v3 == True:
                w_etype, w_evalue = w_13, w_4
                goto = 13
            else:
                goto = 10

        if goto == 10:
            w_15 = space.call_function(space.w_TypeError, w_4)
            w_16 = space.type(w_15)
            w_etype, w_evalue = w_16, w_15
            goto = 13

        if goto == 11:
            w_17 = space.call_function(w_6, )
            w_18 = space.type(w_17)
            w_etype, w_evalue = w_18, w_17
            goto = 13

        if goto == 12:
            w_19 = space.type(w_6)
            w_20 = space.issubtype(w_19, space.w_type)
            v4 = space.is_true(w_20)
            if v4 == True:
                goto = 11
                continue
            else:
                goto = 8
                continue

        if goto == 13:
            raise gOperationError(w_etype, w_evalue)

        if goto == 14:
            return w_8

  fastf_pop = pop
  fastf_pop.__name__ = 'fastf_pop'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'iteritems'
## firstlineno 119
##SECTION##
# global declarations
# global object gdescriptor_dict_items
# global object gs_items

  def iteritems(space, w_d):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function(gdescriptor_dict_items, w_d)
            w_1 = space.iter(w_0)
            goto = 2

        if goto == 2:
            return w_1

  fastf_iteritems = iteritems
  fastf_iteritems.__name__ = 'fastf_iteritems'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'iterkeys'
## firstlineno 122
##SECTION##
# global declarations
# global object g12dict
# global object gs_setdefault
# global object gfunc_setdefault
# global object gs_get
# global object gfunc_get
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_update1
# global object gfunc_update1
# global object gs_update
# global object gfunc_update
# global object gs_pop
# global object gfunc_pop
# global object gs_itervalues
# global object gfunc_itervalues
# global object gs_popitem
# global object gfunc_popitem
# global object gs___name__
# global object gs___builtin__
# global object gs_iteritems
# global object gfunc_iteritems
# global object gs_iterkeys
# global object gfunc_iterkeys
# global object gdescriptor_dict_keys
# global object gs_keys

  def iterkeys(space, w_d):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function(gdescriptor_dict_keys, w_d)
            w_1 = space.iter(w_0)
            goto = 2

        if goto == 2:
            return w_1

  fastf_iterkeys = iterkeys
  fastf_iterkeys.__name__ = 'fastf_iterkeys'

##SECTION##
## filename    'objspace/std/dicttype.py'
## function    'itervalues'
## firstlineno 125
##SECTION##
# global declarations
# global object gdescriptor_dict_values
# global object gs_values

  def itervalues(space, w_d):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function(gdescriptor_dict_values, w_d)
            w_1 = space.iter(w_0)
            goto = 2

        if goto == 2:
            return w_1

  fastf_itervalues = itervalues
  fastf_itervalues.__name__ = 'fastf_itervalues'

##SECTION##
  g12dict = space.newdict()
  gs_setdefault = space.new_interned_str('setdefault')
  from pypy.interpreter import gateway
  gfunc_setdefault = space.wrap(gateway.interp2app(f_setdefault, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g12dict, gs_setdefault, gfunc_setdefault)
  gs_get = space.new_interned_str('get')
  gfunc_get = space.wrap(gateway.interp2app(f_get, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g12dict, gs_get, gfunc_get)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/objspace/std/dicttype.py""")
  space.setitem(g12dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_update1 = space.new_interned_str('update1')
  gfunc_update1 = space.wrap(gateway.interp2app(fastf_update1, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g12dict, gs_update1, gfunc_update1)
  gs_update = space.new_interned_str('update')
  gfunc_update = space.wrap(gateway.interp2app(f_update, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g12dict, gs_update, gfunc_update)
  gs_pop = space.new_interned_str('pop')
  gfunc_pop = space.wrap(gateway.interp2app(fastf_pop, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root, gateway.W_Root]))
  space.setitem(g12dict, gs_pop, gfunc_pop)
  gs_itervalues = space.new_interned_str('itervalues')
  gfunc_itervalues = space.wrap(gateway.interp2app(fastf_itervalues, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g12dict, gs_itervalues, gfunc_itervalues)
  gs_popitem = space.new_interned_str('popitem')
  gfunc_popitem = space.wrap(gateway.interp2app(fastf_popitem, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g12dict, gs_popitem, gfunc_popitem)
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g12dict, gs___name__, gs___builtin__)
  gs_iteritems = space.new_interned_str('iteritems')
  gfunc_iteritems = space.wrap(gateway.interp2app(fastf_iteritems, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g12dict, gs_iteritems, gfunc_iteritems)
  gs_iterkeys = space.new_interned_str('iterkeys')
  gfunc_iterkeys = space.wrap(gateway.interp2app(fastf_iterkeys, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g12dict, gs_iterkeys, gfunc_iterkeys)
  gs_keys = space.new_interned_str('keys')
  gdescriptor_dict_keys = space.getattr(space.w_dict, gs_keys)
  gs_items = space.new_interned_str('items')
  gdescriptor_dict_items = space.getattr(space.w_dict, gs_items)
  gdescriptor_dict_iterkeys = space.getattr(space.w_dict, gs_iterkeys)
  from pypy.interpreter.error import OperationError as gOperationError
  gs_popitem____dictionary_is_empty = space.new_interned_str(
"""popitem(): dictionary is empty""")
  gs___getitem__ = space.new_interned_str('__getitem__')
  gdescriptor_dict___getitem__ = space.getattr(space.w_dict, gs___getitem__)
  gs___delitem__ = space.new_interned_str('__delitem__')
  gdescriptor_dict___delitem__ = space.getattr(space.w_dict, gs___delitem__)
  gs_values = space.new_interned_str('values')
  gdescriptor_dict_values = space.getattr(space.w_dict, gs_values)
  gi_1 = space.wrap(1)
  gs_pop_expected_at_most_2_arguments = space.new_interned_str(
"""pop expected at most 2 arguments, got %d""")
  gi_0 = space.wrap(0)
  gs_update_takes_at_most_1__non_keyw = space.new_interned_str(
"""update takes at most 1 (non-keyword) argument""")
  gs_hasattr = space.new_interned_str('hasattr')
  gs___setitem__ = space.new_interned_str('__setitem__')
  gdescriptor_dict___setitem__ = space.getattr(space.w_dict, gs___setitem__)
  gi_2 = space.wrap(2)
  return g12dict


from pypy._cache import known_code
known_code['f5758cf4dec8f3b09eefeff37088fe7e'] = init__builtin__
