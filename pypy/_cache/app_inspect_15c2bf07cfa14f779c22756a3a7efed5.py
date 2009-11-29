# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'app_inspect_15c2bf07cfa14f779c22756a3a7efed5')
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
Plain Python definition of the builtin functions related to run-time
program introspection.
"""

##SECTION##
## filename    'module/__builtin__/app_inspect.py'
## function    'globals'
## firstlineno 9
##SECTION##
# global declaration
# global object gs_f_globals

  def globals(space):
    """Return the dictionary containing the current scope's global variables."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(mod_sys, gs__getframe)
            w_1 = space.call_function(w_0, gi_0)
            w_2 = space.getattr(w_1, gs_f_globals)
            goto = 2

        if goto == 2:
            return w_2

  fastf_globals = globals
  fastf_globals.__name__ = 'fastf_globals'

##SECTION##
## filename    'module/__builtin__/app_inspect.py'
## function    'locals'
## firstlineno 13
##SECTION##
# global declarations
# global object g11dict
# global object gs__caller_locals
# global object gfunc__caller_locals
# global object gs_vars
# global object gfunc_vars
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs__classdir
# global object gfunc__classdir
# global object gs_sys
# global object mod_sys
# global object bltinmod_helper
# global object gs_globals
# global object gfunc_globals
# global object gs_dir
# global object gfunc_dir
# global object gs___name__
# global object gs___builtin__
# global object gs___doc__
# global object gs_locals
# global object gfunc_locals
# global object gs__getframe
# global object gi_0
# global object gs_f_locals

  def locals(space):
    """Return a dictionary containing the current scope's local variables.
Note that this may be the real dictionary of local variables, or a copy."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(mod_sys, gs__getframe)
            w_1 = space.call_function(w_0, gi_0)
            w_2 = space.getattr(w_1, gs_f_locals)
            goto = 2

        if goto == 2:
            return w_2

  fastf_locals = locals
  fastf_locals.__name__ = 'fastf_locals'

##SECTION##
## filename    'module/__builtin__/app_inspect.py'
## function    '_caller_locals'
## firstlineno 18
##SECTION##
  def _caller_locals(space):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(mod_sys, gs__getframe)
            w_1 = space.call_function(w_0, gi_0)
            w_2 = space.getattr(w_1, gs_f_locals)
            goto = 2

        if goto == 2:
            return w_2

  fastf__caller_locals = _caller_locals
  fastf__caller_locals.__name__ = 'fastf__caller_locals'

##SECTION##
## filename    'module/__builtin__/app_inspect.py'
## function    'vars'
## firstlineno 21
##SECTION##
# global declarations
# global object gs_vars___takes_at_most_1_argument_
# global object gs_vars___argument_must_have___dict

  def vars(space, __args__):
    """Return a dictionary of all the attributes currently bound in obj.  If
    called with no argument, return the variables bound in local scope."""

    funcname = "vars"
    signature = [], 'obj', None
    defaults_w = []
    w_1, = __args__.parse(funcname, signature, defaults_w)
    return fastf_vars(space, w_1)

  f_vars = vars
  f_vars.__name__ = 'f_vars'

  def vars(space, w_1):
    """Return a dictionary of all the attributes currently bound in obj.  If
    called with no argument, return the variables bound in local scope."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_1)
            w_2 = space.eq(w_0, gi_0)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_3 = fastf__caller_locals(space, )
            w_4 = w_3
            goto = 9

        if goto == 3:
            w_5 = space.len(w_1)
            w_6 = space.ne(w_5, gi_1)
            v1 = space.is_true(w_6)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 4:
            w_7 = space.call_function(space.w_TypeError, gs_vars___takes_at_most_1_argument_)
            w_8 = space.type(w_7)
            w_etype, w_evalue = w_8, w_7
            goto = 8

        if goto == 5:
            try:
                w_9 = space.getitem(w_1, gi_0)
                goto = 6
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 7
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 8
                else:raise # unhandled case, should not happen

        if goto == 6:
            try:
                w_10 = space.getattr(w_9, gs___dict__)
                w_4 = w_10
                goto = 9
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 7
                else:raise # unhandled case, should not happen

        if goto == 7:
            w_11 = space.call_function(space.w_TypeError, gs_vars___argument_must_have___dict)
            w_12 = space.type(w_11)
            w_etype, w_evalue = w_12, w_11
            goto = 8

        if goto == 8:
            raise gOperationError(w_etype, w_evalue)

        if goto == 9:
            return w_4

  fastf_vars = vars
  fastf_vars.__name__ = 'fastf_vars'

##SECTION##
## filename    'module/__builtin__/app_inspect.py'
## function    'dir'
## firstlineno 46
##SECTION##
# global declarations
# global object gi_1
# global object gs_dir_expected_at_most_1_arguments
# global object gs_keys
# global object gs_expected_locals___keys___to_be_a
# global object gs_sort
# global object gs___import__
# global object gs_types
# global object g0dict
# global object gs_ModuleType
# global object gs_isinstance
# global object gs___dict__
# global object gs_expected___dict___keys___to_be_a
# global object gs_TypeType
# global object gs_ClassType
# global object gs_update
# global object gs___class__
# global object gs___members__
# global object gs___methods__
# global object gs_StringTypes

  def dir(space, __args__):
    """dir([object]) -> list of strings

    Return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it:

    No argument:  the names in the current scope.
    Module object:  the module attributes.
    Type or class object:  its attributes, and recursively the attributes of
        its bases.
    Otherwise:  its attributes, its class's attributes, and recursively the
        attributes of its class's base classes.
    """

    funcname = "dir"
    signature = [], 'args', None
    defaults_w = []
    w_1, = __args__.parse(funcname, signature, defaults_w)
    return fastf_dir(space, w_1)

  f_dir = dir
  f_dir.__name__ = 'f_dir'

  def dir(space, w_1):
    """dir([object]) -> list of strings

    Return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it:

    No argument:  the names in the current scope.
    Module object:  the module attributes.
    Type or class object:  its attributes, and recursively the attributes of
        its bases.
    Otherwise:  its attributes, its class's attributes, and recursively the
        attributes of its class's base classes.
    """
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_1)
            w_2 = space.gt(w_0, gi_1)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 2
            else:
                goto = 4

        if goto == 2:
            w_3 = space.len(w_1)
            w_4 = space.mod(gs_dir_expected_at_most_1_arguments, w_3)
            w_5 = space.call_function(space.w_TypeError, w_4)
            w_6 = space.type(w_5)
            w_7 = space.issubtype(w_6, space.w_type)
            v1 = space.is_true(w_7)
            if v1 == True:
                goto = 3
            else:
                goto = 6

        if goto == 3:
            w_8 = space.call_function(w_5, )
            w_9 = space.type(w_8)
            w_etype, w_evalue = w_9, w_8
            goto = 46

        if goto == 4:
            w_10 = space.len(w_1)
            w_11 = space.eq(w_10, gi_0)
            v2 = space.is_true(w_11)
            if v2 == True:
                goto = 5
            else:
                goto = 10

        if goto == 5:
            w_12 = fastf__caller_locals(space, )
            w_13 = space.getattr(w_12, gs_keys)
            w_local_names = space.call_function(w_13, )
            w_14 = space.isinstance(w_local_names, space.w_list)
            v3 = space.is_true(w_14)
            if v3 == True:
                goto = 9
            else:
                goto = 7

        if goto == 6:
            w_15 = space.type(w_5)
            w_etype, w_evalue = w_15, w_5
            goto = 46

        if goto == 7:
            w_16 = space.call_function(space.w_TypeError, gs_expected_locals___keys___to_be_a)
            w_17 = space.type(w_16)
            w_18 = space.issubtype(w_17, space.w_type)
            v4 = space.is_true(w_18)
            if v4 == True:
                goto = 8
            else:
                goto = 14

        if goto == 8:
            w_19 = space.call_function(w_16, )
            w_20 = space.type(w_19)
            w_etype, w_evalue = w_20, w_19
            goto = 46

        if goto == 9:
            w_21 = space.getattr(w_local_names, gs_sort)
            w_22 = space.call_function(w_21, )
            w_23 = w_local_names
            goto = 47

        if goto == 10:
            w_types = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs_types, g0dict, space.w_None, space.w_None)
            w_obj = space.getitem(w_1, gi_0)
            w_24 = space.getattr(w_types, gs_ModuleType)
            w_25 = space.call_function((space.builtin.get(space.str_w(gs_isinstance))), w_obj, w_24)
            v5 = space.is_true(w_25)
            if v5 == True:
                goto = 11
            else:
                goto = 25

        if goto == 11:
            try:
                w_26 = space.getattr(w_obj, gs___dict__)
                goto = 12
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                else:raise # unhandled case, should not happen

        if goto == 12:
            try:
                w_27 = space.getattr(w_26, gs_keys)
                goto = 13
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                else:raise # unhandled case, should not happen

        if goto == 13:
            try:
                w_result = space.call_function(w_27, )
                goto = 15
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 14:
            w_28 = space.type(w_16)
            w_etype, w_evalue = w_28, w_16
            goto = 46

        if goto == 15:
            try:
                w_29 = space.isinstance(w_result, space.w_list)
                goto = 16
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 16:
            v6 = space.is_true(w_29)
            if v6 == True:
                goto = 19
            else:
                goto = 17

        if goto == 17:
            try:
                w_30 = space.call_function(space.w_TypeError, gs_expected___dict___keys___to_be_a)
                goto = 18
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 18:
            w_31 = space.type(w_30)
            w_32 = space.issubtype(w_31, space.w_type)
            v7 = space.is_true(w_32)
            if v7 == True:
                goto = 21
            else:
                goto = 28

        if goto == 19:
            try:
                w_33 = space.getattr(w_result, gs_sort)
                goto = 20
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                else:raise # unhandled case, should not happen

        if goto == 20:
            try:
                w_34 = space.call_function(w_33, )
                w_23 = w_result
                goto = 47
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 21:
            try:
                w_35 = space.call_function(w_30, )
                goto = 27
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 24
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 22:
            w_36 = space.issubtype(w_37, space.w_AttributeError)
            v8 = space.is_true(w_36)
            if v8 == True:
                goto = 24
            else:
                w_etype, w_evalue = w_37, w_38
                goto = 46

        if goto == 23:
            w_39 = space.is_(w_37, space.w_AttributeError)
            v9 = space.is_true(w_39)
            if v9 == True:
                goto = 24
            else:
                goto = 22
                continue

        if goto == 24:
            w_40 = space.newlist([])
            w_23 = w_40
            goto = 47

        if goto == 25:
            w_41 = space.getattr(w_types, gs_TypeType)
            w_42 = space.getattr(w_types, gs_ClassType)
            w_43 = space.newtuple([w_41, w_42])
            w_44 = space.call_function((space.builtin.get(space.str_w(gs_isinstance))), w_obj, w_43)
            v10 = space.is_true(w_44)
            if v10 == True:
                goto = 26
            else:
                goto = 29

        if goto == 26:
            w_45 = fastf__classdir(space, w_obj)
            w_46 = space.getattr(w_45, gs_keys)
            w_47 = space.call_function(w_46, )
            w_48 = space.getattr(w_47, gs_sort)
            w_49 = space.call_function(w_48, )
            w_23 = w_47
            goto = 47

        if goto == 27:
            w_50 = space.type(w_35)
            w_37, w_38 = w_50, w_35
            goto = 23
            continue

        if goto == 28:
            w_51 = space.type(w_30)
            w_37, w_38 = w_51, w_30
            goto = 23
            continue

        if goto == 29:
            w_Dict = space.newdict()
            try:
                w_52 = space.getattr(w_Dict, gs_update)
                goto = 30
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 32
                else:raise # unhandled case, should not happen

        if goto == 30:
            try:
                w_53 = space.getattr(w_obj, gs___dict__)
                goto = 31
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 32
                else:raise # unhandled case, should not happen

        if goto == 31:
            try:
                w_54 = space.call_function(w_52, w_53)
                goto = 32
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 32
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 32:
            try:
                w_55 = space.getattr(w_Dict, gs_update)
                goto = 33
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 36
                else:raise # unhandled case, should not happen

        if goto == 33:
            try:
                w_56 = space.getattr(w_obj, gs___class__)
                goto = 34
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 36
                else:raise # unhandled case, should not happen

        if goto == 34:
            try:
                w_57 = fastf__classdir(space, w_56)
                goto = 35
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 36
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 35:
            try:
                w_58 = space.call_function(w_55, w_57)
                goto = 36
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 36
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 36:
            w_59 = space.newlist([gs___members__, gs___methods__])
            w_60 = space.iter(w_59)
            goto = 37

        if goto == 37:
            try:
                w_61 = space.next(w_60)
                goto = 38
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 45
                else:raise # unhandled case, should not happen

        if goto == 38:
            try:
                w_62 = space.getattr(w_obj, w_61)
                goto = 39
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 37
                    continue
                elif e.match(space, space.w_TypeError):
                    goto = 37
                    continue
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 39:
            w_63 = space.iter(w_62)
            goto = 40

        if goto == 40:
            try:
                w_item = space.next(w_63)
                goto = 41
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 37
                    continue
                else:raise # unhandled case, should not happen

        if goto == 41:
            try:
                w_64 = space.getattr(w_types, gs_StringTypes)
                goto = 42
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 37
                    continue
                else:raise # unhandled case, should not happen

        if goto == 42:
            try:
                w_65 = space.call_function((space.builtin.get(space.str_w(gs_isinstance))), w_item, w_64)
                goto = 43
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 37
                    continue
                elif e.match(space, space.w_TypeError):
                    goto = 37
                    continue
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 43:
            v11 = space.is_true(w_65)
            if v11 == True:
                goto = 44
            else:
                goto = 40
                continue

        if goto == 44:
            try:
                w_66 = space.setitem(w_Dict, w_item, space.w_None)
                goto = 40
                continue
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 37
                    continue
                elif e.match(space, space.w_TypeError):
                    goto = 37
                    continue
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 46
                else:raise # unhandled case, should not happen

        if goto == 45:
            w_67 = space.getattr(w_Dict, gs_keys)
            w_68 = space.call_function(w_67, )
            w_69 = space.getattr(w_68, gs_sort)
            w_70 = space.call_function(w_69, )
            w_23 = w_68
            goto = 47

        if goto == 46:
            raise gOperationError(w_etype, w_evalue)

        if goto == 47:
            return w_23

  fastf_dir = dir
  fastf_dir.__name__ = 'fastf_dir'

##SECTION##
## filename    'module/__builtin__/app_inspect.py'
## function    '_classdir'
## firstlineno 113
##SECTION##
# global declaration
# global object gs___bases__

  def _classdir(space, w_klass):
    """Return a dict of the accessible attributes of class/type klass.

    This includes all attributes of klass and all of the
    base classes recursively.

    The values of this dict have no meaning - only the keys have
    meaning.  
    """
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_Dict = space.newdict()
            try:
                w_0 = space.getattr(w_Dict, gs_update)
                goto = 2
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 4
                else:raise # unhandled case, should not happen

        if goto == 2:
            try:
                w_1 = space.getattr(w_klass, gs___dict__)
                goto = 3
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 4
                else:raise # unhandled case, should not happen

        if goto == 3:
            try:
                w_2 = space.call_function(w_0, w_1)
                goto = 4
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 4
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 10
                else:raise # unhandled case, should not happen

        if goto == 4:
            try:
                w_3 = space.getattr(w_klass, gs___bases__)
                goto = 5
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 5:
            w_4 = space.iter(w_3)
            goto = 6

        if goto == 6:
            try:
                w_base = space.next(w_4)
                goto = 7
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 7:
            w_5 = space.getattr(w_Dict, gs_update)
            try:
                w_6 = fastf__classdir(space, w_base)
                goto = 8
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_TypeError):
                    goto = 9
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 10
                else:raise # unhandled case, should not happen

        if goto == 8:
            try:
                w_7 = space.call_function(w_5, w_6)
                goto = 6
                continue
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_TypeError):
                    goto = 9
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 10
                else:raise # unhandled case, should not happen

        if goto == 9:
            return w_Dict

        if goto == 10:
            raise gOperationError(w_etype, w_evalue)

  fastf__classdir = _classdir
  fastf__classdir.__name__ = 'fastf__classdir'

##SECTION##
  w__doc__ = space.new_interned_str(__doc__)
  g11dict = space.newdict()
  gs__caller_locals = space.new_interned_str('_caller_locals')
  from pypy.interpreter import gateway
  gfunc__caller_locals = space.wrap(gateway.interp2app(fastf__caller_locals, unwrap_spec=[gateway.ObjSpace, ]))
  space.setitem(g11dict, gs__caller_locals, gfunc__caller_locals)
  gs_vars = space.new_interned_str('vars')
  gfunc_vars = space.wrap(gateway.interp2app(f_vars, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g11dict, gs_vars, gfunc_vars)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/module/__builtin__/app_inspect.py""")
  space.setitem(g11dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs__classdir = space.new_interned_str('_classdir')
  gfunc__classdir = space.wrap(gateway.interp2app(fastf__classdir, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g11dict, gs__classdir, gfunc__classdir)
  gs_sys = space.new_interned_str('sys')
  def bltinmod_helper(name):
      dic = space.newdict()
      space.exec_("import %s" % name, dic, dic, hidden_applevel=True)
      return space.eval("%s" % name, dic, dic, hidden_applevel=True)
  mod_sys = bltinmod_helper('sys')
  space.setitem(g11dict, gs_sys, mod_sys)
  gs_globals = space.new_interned_str('globals')
  gfunc_globals = space.wrap(gateway.interp2app(fastf_globals, unwrap_spec=[gateway.ObjSpace, ]))
  space.setitem(g11dict, gs_globals, gfunc_globals)
  gs_dir = space.new_interned_str('dir')
  gfunc_dir = space.wrap(gateway.interp2app(f_dir, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g11dict, gs_dir, gfunc_dir)
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g11dict, gs___name__, gs___builtin__)
  gs___doc__ = space.new_interned_str('__doc__')
  space.setitem(g11dict, gs___doc__, w__doc__)
  gs_locals = space.new_interned_str('locals')
  gfunc_locals = space.wrap(gateway.interp2app(fastf_locals, unwrap_spec=[gateway.ObjSpace, ]))
  space.setitem(g11dict, gs_locals, gfunc_locals)
  gs__getframe = space.new_interned_str('_getframe')
  gi_0 = space.wrap(0)
  gs_f_locals = space.new_interned_str('f_locals')
  gi_1 = space.wrap(1)
  gs_dir_expected_at_most_1_arguments = space.new_interned_str(
"""dir expected at most 1 arguments, got %d""")
  gs_keys = space.new_interned_str('keys')
  gs_expected_locals___keys___to_be_a = space.new_interned_str(
"""expected locals().keys() to be a list""")
  gs_sort = space.new_interned_str('sort')
  gs___import__ = space.new_interned_str('__import__')
  gs_types = space.new_interned_str('types')
  g0dict = space.newdict()
  gs_ModuleType = space.new_interned_str('ModuleType')
  gs_isinstance = space.new_interned_str('isinstance')
  gs___dict__ = space.new_interned_str('__dict__')
  from pypy.interpreter.error import OperationError as gOperationError
  gs_expected___dict___keys___to_be_a = space.new_interned_str(
"""expected __dict__.keys() to be a list""")
  gs_TypeType = space.new_interned_str('TypeType')
  gs_ClassType = space.new_interned_str('ClassType')
  gs_update = space.new_interned_str('update')
  gs___class__ = space.new_interned_str('__class__')
  gs___members__ = space.new_interned_str('__members__')
  gs___methods__ = space.new_interned_str('__methods__')
  gs_StringTypes = space.new_interned_str('StringTypes')
  gs_f_globals = space.new_interned_str('f_globals')
  gs___bases__ = space.new_interned_str('__bases__')
  gs_vars___takes_at_most_1_argument_ = space.new_interned_str(
"""vars() takes at most 1 argument.""")
  gs_vars___argument_must_have___dict = space.new_interned_str(
"""vars() argument must have __dict__ attribute""")
  return g11dict


from pypy._cache import known_code
known_code['15c2bf07cfa14f779c22756a3a7efed5'] = init__builtin__
