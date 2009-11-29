# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'app_misc_e55dd86728fa64d149beed048360c640')
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

  __doc__ = \
"""
Plain Python definition of some miscellaneous builtin functions.
"""

##SECTION##
## filename    'module/__builtin__/app_misc.py'
## function    'find_module'
## firstlineno 7
##SECTION##
# global declarations
# global object gs_meta_path
# global object gs_path
# global object gs_path_hooks
# global object gs_path_importer_cache
# global object gs_get

  def find_module(space, w_fullname, w_path):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_sys = space.getbuiltinmodule('sys')
            w_0 = space.getattr(w_sys, gs_meta_path)
            w_1 = space.iter(w_0)
            goto = 2

        if goto == 2:
            try:
                w_2 = space.next(w_1)
                goto = 3
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 4
                else:raise # unhandled case, should not happen

        if goto == 3:
            w_3 = space.getattr(w_2, gs_find_module)
            w_4 = space.call_function(w_3, w_fullname, w_path)
            v0 = space.is_true(w_4)
            if v0 == True:
                w_5 = w_4
                goto = 20
            else:
                goto = 2
                continue

        if goto == 4:
            w_6 = space.ne(w_path, space.w_None)
            v1 = space.is_true(w_6)
            if v1 == True:
                goto = 5
            else:
                goto = 6

        if goto == 5:
            w_7 = space.type(w_path)
            w_8 = space.eq(w_7, space.w_str)
            v2 = space.is_true(w_8)
            if v2 == True:
                goto = 6
            else:
                goto = 6

        if goto == 6:
            w_9 = space.eq(w_path, space.w_None)
            v3 = space.is_true(w_9)
            if v3 == True:
                goto = 7
            else:
                w_path_1 = w_path
                goto = 8

        if goto == 7:
            w_10 = space.getattr(w_sys, gs_path)
            w_path_1 = w_10
            goto = 8

        if goto == 8:
            w_path_hooks = space.getattr(w_sys, gs_path_hooks)
            w_importer_cache = space.getattr(w_sys, gs_path_importer_cache)
            w_11 = space.iter(w_path_1)
            goto = 9

        if goto == 9:
            try:
                w_12 = space.next(w_11)
                goto = 10
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_5 = space.w_None
                    goto = 20
                else:raise # unhandled case, should not happen

        if goto == 10:
            w_13 = space.getattr(w_importer_cache, gs_get)
            w_14 = space.call_function(w_13, w_12, space.w_None)
            v4 = space.is_true(w_14)
            if v4 == True:
                goto = 11
            else:
                goto = 12

        if goto == 11:
            w_15 = space.getattr(w_importer_cache, gs_get)
            w_16 = space.call_function(w_15, w_12)
            w_17 = w_16
            goto = 17

        if goto == 12:
            w_18 = space.setitem(w_importer_cache, w_12, space.w_None)
            w_19 = space.iter(w_path_hooks)
            goto = 13

        if goto == 13:
            try:
                w_20 = space.next(w_19)
                goto = 14
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 9
                    continue
                else:raise # unhandled case, should not happen

        if goto == 14:
            try:
                w_importer = space.call_function(w_20, w_12)
                goto = 15
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_ImportError):
                    goto = 13
                    continue
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 19
                else:raise # unhandled case, should not happen

        if goto == 15:
            v5 = space.is_true(w_importer)
            if v5 == True:
                goto = 16
            else:
                w_17 = w_importer
                goto = 17

        if goto == 16:
            w_21 = space.setitem(w_importer_cache, w_12, w_importer)
            w_17 = w_importer
            goto = 17

        if goto == 17:
            v6 = space.is_true(w_17)
            if v6 == True:
                goto = 18
            else:
                goto = 9
                continue

        if goto == 18:
            w_22 = space.getattr(w_17, gs_find_module)
            w_23 = space.call_function(w_22, w_fullname)
            v7 = space.is_true(w_23)
            if v7 == True:
                w_5 = w_23
                goto = 20
            else:
                goto = 9
                continue

        if goto == 19:
            raise gOperationError(w_etype, w_evalue)

        if goto == 20:
            return w_5

  fastf_find_module = find_module
  fastf_find_module.__name__ = 'fastf_find_module'

##SECTION##
## filename    'module/__builtin__/app_misc.py'
## function    'reload'
## firstlineno 44
##SECTION##
# global declarations
# global object g6dict
# global object gs_find_module
# global object gfunc_find_module
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_reload
# global object gfunc_reload
# global object gs___name__
# global object gs___builtin__
# global object gs___doc__
# global object gs___import__
# global object gs_imp
# global object g0dict
# global object gs_errno
# global object g0dict_1
# global object gs_reload___argument_must_be_module
# global object gs_modules
# global object gs_reload____module___200s_not_in_s
# global object gs_split
# global object gs__
# global object gi_minus_1
# global object gbltinmethod_join
# global object gs_join
# global object gs_reload____parent___200s_not_in_s
# global object gs___path__
# global object gs_load_module
# global object gi_3
# global object gi_0
# global object gi_1
# global object gi_2
# global object gs_close

  def reload(space, w_module):
    """Reload the module.
    The module must have been successfully imported before."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_imp = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs_imp, g0dict, space.w_None, space.w_None)
            w_sys = space.getbuiltinmodule('sys')
            w_0 = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs_errno, g0dict_1, space.w_None, space.w_None)
            w_1 = space.type(w_module)
            w_2 = space.type(w_imp)
            w_3 = space.type(w_0)
            w_4 = space.newtuple([w_2, w_3])
            w_5 = space.contains(w_4, w_1)
            v0 = space.is_true(w_5)
            if v0 == True:
                goto = 4
            else:
                goto = 2

        if goto == 2:
            w_6 = space.call_function(space.w_TypeError, gs_reload___argument_must_be_module)
            w_7 = space.type(w_6)
            w_8 = space.issubtype(w_7, space.w_type)
            v1 = space.is_true(w_8)
            if v1 == True:
                goto = 3
            else:
                goto = 5

        if goto == 3:
            w_9 = space.call_function(w_6, )
            w_10 = space.type(w_9)
            w_etype, w_evalue = w_10, w_9
            goto = 25

        if goto == 4:
            w_name = space.getattr(w_module, gs___name__)
            w_11 = space.getattr(w_sys, gs_modules)
            w_12 = space.getitem(w_11, w_name)
            w_13 = space.is_(w_module, w_12)
            v2 = space.is_true(w_13)
            if v2 == True:
                goto = 8
            else:
                goto = 6

        if goto == 5:
            w_14 = space.type(w_6)
            w_etype, w_evalue = w_14, w_6
            goto = 25

        if goto == 6:
            w_15 = space.mod(gs_reload____module___200s_not_in_s, w_name)
            w_16 = space.call_function(space.w_ImportError, w_15)
            w_17 = space.type(w_16)
            w_18 = space.issubtype(w_17, space.w_type)
            v3 = space.is_true(w_18)
            if v3 == True:
                goto = 7
            else:
                goto = 9

        if goto == 7:
            w_19 = space.call_function(w_16, )
            w_20 = space.type(w_19)
            w_etype, w_evalue = w_20, w_19
            goto = 25

        if goto == 8:
            w_21 = space.getattr(w_name, gs_split)
            w_22 = space.call_function(w_21, gs__)
            w_subname = space.getitem(w_22, gi_minus_1)
            w_23 = space.getslice(w_22, space.w_None, gi_minus_1)
            w_parent_name = space.call_function(gbltinmethod_join, w_23)
            v4 = space.is_true(w_parent_name)
            if v4 == True:
                goto = 10
            else:
                w_path = space.w_None
                goto = 14

        if goto == 9:
            w_24 = space.type(w_16)
            w_etype, w_evalue = w_24, w_16
            goto = 25

        if goto == 10:
            w_25 = space.getattr(w_sys, gs_modules)
            try:
                w_26 = space.getitem(w_25, w_parent_name)
                goto = 13
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_KeyError):
                    goto = 11
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 25
                else:raise # unhandled case, should not happen

        if goto == 11:
            w_27 = space.mod(gs_reload____parent___200s_not_in_s, w_parent_name)
            w_28 = space.call_function(space.w_ImportError, w_27)
            w_29 = space.type(w_28)
            w_30 = space.issubtype(w_29, space.w_type)
            v5 = space.is_true(w_30)
            if v5 == True:
                goto = 12
            else:
                goto = 16

        if goto == 12:
            w_31 = space.call_function(w_28, )
            w_32 = space.type(w_31)
            w_etype, w_evalue = w_32, w_31
            goto = 25

        if goto == 13:
            w_33 = space.getattr(w_26, gs___path__)
            w_path = w_33
            goto = 14

        if goto == 14:
            w_34 = fastf_find_module(space, w_name, w_path)
            v6 = space.is_true(w_34)
            if v6 == True:
                goto = 15
            else:
                goto = 17

        if goto == 15:
            w_35 = space.getattr(w_34, gs_load_module)
            w_36 = space.call_function(w_35, w_name)
            v7 = space.is_true(w_36)
            if v7 == True:
                w_37 = w_36
                goto = 26
            else:
                goto = 17

        if goto == 16:
            w_38 = space.type(w_28)
            w_etype, w_evalue = w_38, w_28
            goto = 25

        if goto == 17:
            w_39 = space.getattr(w_imp, gs_find_module)
            w_40 = space.call_function(w_39, w_subname, w_path)
            w_41 = space.len(w_40)
            w_42 = space.eq(w_41, gi_3)
            v8 = space.is_true(w_42)
            if v8 == True:
                goto = 20
            else:
                goto = 19

        if goto == 18:
            try:
                w_new_module = space.call_function(w_43, w_name, w_f, w_44, w_45)
                goto = 21
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_Exception):
                    w_46, w_47 = e.w_type, e.w_value
                    goto = 22
                else:raise # unhandled case, should not happen

        if goto == 19:
            w_48 = space.call_function(space.w_ValueError, )
            w_49 = space.type(w_48)
            w_etype, w_evalue = w_49, w_48
            goto = 25

        if goto == 20:
            w_f = space.getitem(w_40, gi_0)
            w_44 = space.getitem(w_40, gi_1)
            w_45 = space.getitem(w_40, gi_2)
            try:
                w_43 = space.getattr(w_imp, gs_load_module)
                goto = 18
                continue
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    w_46, w_47 = e.w_type, e.w_value
                    goto = 22
                else:raise # unhandled case, should not happen

        if goto == 21:
            w_50 = space.getattr(w_sys, gs_modules)
            w_51 = space.setitem(w_50, w_name, w_module)
            w_52 = space.is_(w_f, space.w_None)
            v9 = space.is_true(w_52)
            if v9 == True:
                w_37 = w_new_module
                goto = 26
            else:
                goto = 23

        if goto == 22:
            w_53 = space.getattr(w_sys, gs_modules)
            w_54 = space.setitem(w_53, w_name, w_module)
            w_55 = space.is_(w_f, space.w_None)
            v10 = space.is_true(w_55)
            if v10 == True:
                w_etype, w_evalue = w_46, w_47
                goto = 25
            else:
                goto = 24

        if goto == 23:
            w_56 = space.getattr(w_f, gs_close)
            w_57 = space.call_function(w_56, )
            w_37 = w_new_module
            goto = 26

        if goto == 24:
            w_58 = space.getattr(w_f, gs_close)
            w_59 = space.call_function(w_58, )
            w_etype, w_evalue = w_46, w_47
            goto = 25

        if goto == 25:
            raise gOperationError(w_etype, w_evalue)

        if goto == 26:
            return w_37

  fastf_reload = reload
  fastf_reload.__name__ = 'fastf_reload'

##SECTION##
  w__doc__ = space.new_interned_str(__doc__)
  g6dict = space.newdict()
  gs_find_module = space.new_interned_str('find_module')
  from pypy.interpreter import gateway
  gfunc_find_module = space.wrap(gateway.interp2app(fastf_find_module, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g6dict, gs_find_module, gfunc_find_module)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/module/__builtin__/app_misc.py""")
  space.setitem(g6dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_reload = space.new_interned_str('reload')
  gfunc_reload = space.wrap(gateway.interp2app(fastf_reload, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g6dict, gs_reload, gfunc_reload)
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g6dict, gs___name__, gs___builtin__)
  gs___doc__ = space.new_interned_str('__doc__')
  space.setitem(g6dict, gs___doc__, w__doc__)
  gs___import__ = space.new_interned_str('__import__')
  gs_imp = space.new_interned_str('imp')
  g0dict = space.newdict()
  gs_errno = space.new_interned_str('errno')
  g0dict_1 = space.newdict()
  gs_reload___argument_must_be_module = space.new_interned_str(
"""reload() argument must be module""")
  gs_modules = space.new_interned_str('modules')
  gs_reload____module___200s_not_in_s = space.new_interned_str(
"""reload(): module %.200s not in sys.modules""")
  gs_split = space.new_interned_str('split')
  gs__ = space.new_interned_str('.')
  gi_minus_1 = space.wrap(-1)
  gs_join = space.new_interned_str('join')
  gbltinmethod_join = space.getattr(gs__, gs_join)
  from pypy.interpreter.error import OperationError as gOperationError
  gs_reload____parent___200s_not_in_s = space.new_interned_str(
"""reload(): parent %.200s not in sys.modules""")
  gs___path__ = space.new_interned_str('__path__')
  gs_load_module = space.new_interned_str('load_module')
  gi_3 = space.wrap(3)
  gi_0 = space.wrap(0)
  gi_1 = space.wrap(1)
  gi_2 = space.wrap(2)
  gs_close = space.new_interned_str('close')
  gs_meta_path = space.new_interned_str('meta_path')
  gs_path = space.new_interned_str('path')
  gs_path_hooks = space.new_interned_str('path_hooks')
  gs_path_importer_cache = space.new_interned_str('path_importer_cache')
  gs_get = space.new_interned_str('get')
  return g6dict


from pypy._cache import known_code
known_code['e55dd86728fa64d149beed048360c640'] = init__builtin__
