# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], '_exceptions_79773bc75ab921298d30069185ff81ee')
    for ending in ('.py', '.pyc', '.pyo'):
        try:
            os.unlink(namestart+ending)
        except os.error:
            pass

#!/bin/env python
# -*- coding: LATIN-1 -*-

#*************************************************************
__name__ = "_geninterp_"+'exceptions'
_geninterp_ = True

def initexceptions(space):
  """NOT_RPYTHON"""

  __doc__ = \
"""Python's standard exception class hierarchy.

Before Python 1.5, the standard exceptions were all simple string objects.
In Python 1.5, the standard exceptions were converted to classes organized
into a relatively flat hierarchy.  String-based standard exceptions were
optional, or used as a fallback if some problem occurred while importing
the exception module.  With Python 1.6, optional string-based standard
exceptions were removed (along with the -X command line flag).

The class exceptions were implemented in such a way as to be almost
completely backward compatible.  Some tricky uses of IOError could
potentially have broken, but by Python 1.6, all of these should have
been fixed.  As of Python 1.6, the class-based standard exceptions are
now implemented in C, and are guaranteed to exist in the Python
interpreter.

Here is a rundown of the class hierarchy.  The classes found here are
inserted into both the exceptions module and the `built-in' module.  It is
recommended that user defined class based exceptions be derived from the
`Exception' class, although this is currently not enforced.

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception
      +-- GeneratorExit
      +-- StopIteration
      +-- StandardError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |    |    +-- UnicodeError
      |    |         +-- UnicodeDecodeError
      |    |         +-- UnicodeEncodeError
      |    |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
"""

# global declarations
# global object g50dict
# global object gs_GeneratorExit
# global object gcls_GeneratorExit
# global object gcls_Exception
# global object gcls_BaseException
# global object gs___module__
# global object gs_exceptions
# global object gs___doc__
# global object gs_BaseException
# global object gs_Exception
# global object gs_ImportError
# global object gcls_ImportError
# global object gcls_StandardError
# global object gs_StandardError
# global object gs_RuntimeError
# global object gcls_RuntimeError
# global object gs_UnicodeTranslateError
# global object gcls_UnicodeTranslateError
# global object gcls_UnicodeError
# global object gcls_ValueError
# global object gs_ValueError
# global object gs_UnicodeError
# global object gs_KeyError
# global object gcls_KeyError
# global object gcls_LookupError
# global object gs_LookupError
# global object gs_SyntaxWarning
# global object gcls_SyntaxWarning
# global object gcls_Warning
# global object gs_Warning
# global object gs_StopIteration
# global object gcls_StopIteration
# global object gs_PendingDeprecationWarning
# global object gcls_PendingDeprecationWarning
# global object gs_EnvironmentError
# global object gcls_EnvironmentError
# global object gs_OSError
# global object gcls_OSError
# global object gs_DeprecationWarning
# global object gcls_DeprecationWarning
# global object gs_FloatingPointError
# global object gcls_FloatingPointError
# global object gcls_ArithmeticError
# global object gs_ArithmeticError
# global object gs_UnicodeWarning
# global object gcls_UnicodeWarning
# global object gs_AttributeError
# global object gcls_AttributeError
# global object gs_IndentationError
# global object gcls_IndentationError
# global object gcls_SyntaxError
# global object gs_SyntaxError
# global object gs_NameError
# global object gcls_NameError
# global object gs_IOError
# global object gcls_IOError
# global object gs_FutureWarning
# global object gcls_FutureWarning
# global object gs_ImportWarning
# global object gcls_ImportWarning
# global object gs_SystemExit
# global object gcls_SystemExit
# global object gs_EOFError
# global object gcls_EOFError
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_TabError
# global object gcls_TabError
# global object gs_UnicodeEncodeError
# global object gcls_UnicodeEncodeError
# global object gs_UnboundLocalError
# global object gcls_UnboundLocalError
# global object gs___name__
# global object gs_ReferenceError
# global object gcls_ReferenceError
# global object gs_AssertionError
# global object gcls_AssertionError
# global object gs_UnicodeDecodeError
# global object gcls_UnicodeDecodeError
# global object gs_TypeError
# global object gcls_TypeError
# global object gs_IndexError
# global object gcls_IndexError
# global object gs_RuntimeWarning
# global object gcls_RuntimeWarning
# global object gs_KeyboardInterrupt
# global object gcls_KeyboardInterrupt
# global object gs_UserWarning
# global object gcls_UserWarning
# global object gs_ZeroDivisionError
# global object gcls_ZeroDivisionError
# global object gs_MemoryError
# global object gcls_MemoryError
# global object gs_NotImplementedError
# global object gcls_NotImplementedError
# global object gs_SystemError
# global object gcls_SystemError
# global object gs_OverflowError
# global object gcls_OverflowError
# global object gs___init__
# global object gfunc_UnicodeDecodeError___init__
# global object gs___str__
# global object gfunc_UnicodeDecodeError___str__
# global object gfunc_UnicodeEncodeError___init__
# global object gfunc_UnicodeEncodeError___str__
# global object gfunc_SystemExit___init__
# global object gfunc_SyntaxError___init__
# global object gfunc_SyntaxError___str__
# global object gs_filename
# global object gs_lineno
# global object gs_msg
# global object gs__emptystr_
# global object gs_offset
# global object gs_print_file_and_line
# global object gs_text
# global object gfunc_EnvironmentError___init__
# global object gfunc_EnvironmentError___str__
# global object gfunc_KeyError___str__
# global object gfunc_UnicodeTranslateError___init__
# global object gfunc_UnicodeTranslateError___str__
# global object gs___getitem__
# global object gfunc_BaseException___getitem__
# global object gfunc_BaseException___init__
# global object gs___repr__
# global object gfunc_BaseException___repr__
# global object gfunc_BaseException___str__

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__getitem__'
## firstlineno 79
##SECTION##
  def __getitem__(space, w_self, w_idx):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_args)
            w_1 = space.getitem(w_0, w_idx)
            goto = 2

        if goto == 2:
            return w_1

  fastf_BaseException___getitem__ = __getitem__
  fastf_BaseException___getitem__.__name__ = 'fastf_BaseException___getitem__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__init__'
## firstlineno 82
##SECTION##
# global declaration
# global object gs_message

  def __init__(space, __args__):
    funcname = "__init__"
    signature = ['self'], 'args', None
    defaults_w = []
    w_1, w_2 = __args__.parse(funcname, signature, defaults_w)
    return fastf_BaseException___init__(space, w_1, w_2)

  f_BaseException___init__ = __init__
  f_BaseException___init__.__name__ = 'f_BaseException___init__'

  def __init__(space, w_1, w_2):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.setattr(w_1, gs_args, w_2)
            w_3 = space.len(w_2)
            w_4 = space.eq(w_3, gi_1)
            v0 = space.is_true(w_4)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_5 = space.getitem(w_2, gi_0)
            w_6 = space.setattr(w_1, gs_message, w_5)
            w_7 = space.w_None
            goto = 4

        if goto == 3:
            w_8 = space.setattr(w_1, gs_message, gs__emptystr_)
            w_7 = space.w_None
            goto = 4

        if goto == 4:
            return w_7

  fastf_BaseException___init__ = __init__
  fastf_BaseException___init__.__name__ = 'fastf_BaseException___init__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__str__'
## firstlineno 89
##SECTION##
# global declarations
# global object gs_args
# global object gi_0
# global object gi_1

  def __str__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_args = space.getattr(w_self, gs_args)
            w_0 = space.len(w_args)
            w_1 = space.eq(w_0, gi_0)
            v0 = space.is_true(w_1)
            if v0 == True:
                w_2 = gs__emptystr_
                goto = 5
            else:
                goto = 2

        if goto == 2:
            w_3 = space.eq(w_0, gi_1)
            v1 = space.is_true(w_3)
            if v1 == True:
                goto = 3
            else:
                goto = 4

        if goto == 3:
            w_4 = space.getitem(w_args, gi_0)
            w_5 = space.str(w_4)
            w_2 = w_5
            goto = 5

        if goto == 4:
            w_6 = space.str(w_args)
            w_2 = w_6
            goto = 5

        if goto == 5:
            return w_2

  fastf_BaseException___str__ = __str__
  fastf_BaseException___str__.__name__ = 'fastf_BaseException___str__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__repr__'
## firstlineno 99
##SECTION##
# global declarations
# global object gs___
# global object gs___class__

  def __repr__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_args)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                w_func_args = gs___
                goto = 3

        if goto == 2:
            w_1 = space.getattr(w_self, gs_args)
            w_2 = space.repr(w_1)
            w_func_args = w_2
            goto = 3

        if goto == 3:
            w_3 = space.getattr(w_self, gs___class__)
            w_4 = space.getattr(w_3, gs___name__)
            w_5 = space.add(w_4, w_func_args)
            goto = 4

        if goto == 4:
            return w_5

  fastf_BaseException___repr__ = __repr__
  fastf_BaseException___repr__.__name__ = 'fastf_BaseException___repr__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__init__'
## firstlineno 131
##SECTION##
# global declarations
# global object gi_4
# global object gs_argument_0_must_be_unicode__not_
# global object gi_2
# global object gs_argument_1_must_be_int__not__s
# global object gi_3
# global object gs_argument_2_must_be_int__not__s
# global object gs_argument_3_must_be_str__not__s
# global object gs_function_takes_exactly_4_argumen

  def __init__(space, __args__):
    funcname = "__init__"
    signature = ['self'], 'args', None
    defaults_w = []
    w_self, w_args = __args__.parse(funcname, signature, defaults_w)
    return fastf_UnicodeTranslateError___init__(space, w_self, w_args)

  f_UnicodeTranslateError___init__ = __init__
  f_UnicodeTranslateError___init__.__name__ = 'f_UnicodeTranslateError___init__'

  def __init__(space, w_self, w_args):
    goto = 1 # startblock
    while True:

        if goto == 1:
            _args = gateway.Arguments.fromshape(space, (1, [], True, False), [w_self, w_args])
            w_0 = space.call_args(gfunc_BaseException___init__, _args)
            w_1 = space.len(w_args)
            w_2 = space.setattr(w_self, gs_args, w_args)
            w_3 = space.eq(w_1, gi_4)
            v0 = space.is_true(w_3)
            if v0 == True:
                goto = 2
            else:
                goto = 20

        if goto == 2:
            w_4 = space.getitem(w_args, gi_0)
            w_5 = space.type(w_4)
            w_6 = space.eq(w_5, space.w_unicode)
            v1 = space.is_true(w_6)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 3:
            w_7 = space.type(w_8)
            w_etype, w_evalue = w_7, w_8
            goto = 22

        if goto == 4:
            w_9 = space.getitem(w_args, gi_0)
            w_10 = space.setattr(w_self, gs_object, w_9)
            w_11 = space.getitem(w_args, gi_1)
            w_12 = space.type(w_11)
            w_13 = space.eq(w_12, space.w_int)
            v2 = space.is_true(w_13)
            if v2 == True:
                goto = 8
            else:
                goto = 9

        if goto == 5:
            w_14 = space.getitem(w_args, gi_0)
            w_15 = space.type(w_14)
            w_16 = space.mod(gs_argument_0_must_be_unicode__not_, w_15)
            w_17 = space.call_function(gcls_TypeError, w_16)
            w_18 = space.type(w_17)
            w_19 = space.issubtype(w_18, space.w_type)
            v3 = space.is_true(w_19)
            if v3 == True:
                goto = 6
            else:
                goto = 7

        if goto == 6:
            w_20 = space.call_function(w_17, )
            w_21 = space.type(w_20)
            w_etype, w_evalue = w_21, w_20
            goto = 22

        if goto == 7:
            w_22 = space.type(w_17)
            w_etype, w_evalue = w_22, w_17
            goto = 22

        if goto == 8:
            w_23 = space.getitem(w_args, gi_1)
            w_24 = space.setattr(w_self, gs_start, w_23)
            w_25 = space.getitem(w_args, gi_2)
            w_26 = space.type(w_25)
            w_27 = space.eq(w_26, space.w_int)
            v4 = space.is_true(w_27)
            if v4 == True:
                goto = 12
            else:
                goto = 13

        if goto == 9:
            w_28 = space.getitem(w_args, gi_1)
            w_29 = space.type(w_28)
            w_30 = space.mod(gs_argument_1_must_be_int__not__s, w_29)
            w_31 = space.call_function(gcls_TypeError, w_30)
            w_32 = space.type(w_31)
            w_33 = space.issubtype(w_32, space.w_type)
            v5 = space.is_true(w_33)
            if v5 == True:
                goto = 10
            else:
                goto = 11

        if goto == 10:
            w_34 = space.call_function(w_31, )
            w_35 = space.type(w_34)
            w_etype, w_evalue = w_35, w_34
            goto = 22

        if goto == 11:
            w_36 = space.type(w_31)
            w_etype, w_evalue = w_36, w_31
            goto = 22

        if goto == 12:
            w_37 = space.getitem(w_args, gi_2)
            w_38 = space.setattr(w_self, gs_end, w_37)
            w_39 = space.getitem(w_args, gi_3)
            w_40 = space.type(w_39)
            w_41 = space.eq(w_40, space.w_str)
            v6 = space.is_true(w_41)
            if v6 == True:
                goto = 16
            else:
                goto = 17

        if goto == 13:
            w_42 = space.getitem(w_args, gi_2)
            w_43 = space.type(w_42)
            w_44 = space.mod(gs_argument_2_must_be_int__not__s, w_43)
            w_45 = space.call_function(gcls_TypeError, w_44)
            w_46 = space.type(w_45)
            w_47 = space.issubtype(w_46, space.w_type)
            v7 = space.is_true(w_47)
            if v7 == True:
                goto = 14
            else:
                goto = 15

        if goto == 14:
            w_48 = space.call_function(w_45, )
            w_49 = space.type(w_48)
            w_etype, w_evalue = w_49, w_48
            goto = 22

        if goto == 15:
            w_50 = space.type(w_45)
            w_etype, w_evalue = w_50, w_45
            goto = 22

        if goto == 16:
            w_51 = space.getitem(w_args, gi_3)
            w_52 = space.setattr(w_self, gs_reason, w_51)
            w_53 = space.w_None
            goto = 23

        if goto == 17:
            w_54 = space.getitem(w_args, gi_3)
            w_55 = space.type(w_54)
            w_56 = space.mod(gs_argument_3_must_be_str__not__s, w_55)
            w_57 = space.call_function(gcls_TypeError, w_56)
            w_58 = space.type(w_57)
            w_59 = space.issubtype(w_58, space.w_type)
            v8 = space.is_true(w_59)
            if v8 == True:
                goto = 19
            else:
                goto = 18

        if goto == 18:
            w_60 = space.type(w_57)
            w_etype, w_evalue = w_60, w_57
            goto = 22

        if goto == 19:
            w_61 = space.call_function(w_57, )
            w_62 = space.type(w_61)
            w_etype, w_evalue = w_62, w_61
            goto = 22

        if goto == 20:
            w_63 = space.mod(gs_function_takes_exactly_4_argumen, w_1)
            w_8 = space.call_function(gcls_TypeError, w_63)
            w_64 = space.type(w_8)
            w_65 = space.issubtype(w_64, space.w_type)
            v9 = space.is_true(w_65)
            if v9 == True:
                goto = 21
            else:
                goto = 3
                continue

        if goto == 21:
            w_66 = space.call_function(w_8, )
            w_67 = space.type(w_66)
            w_etype, w_evalue = w_67, w_66
            goto = 22

        if goto == 22:
            raise gOperationError(w_etype, w_evalue)

        if goto == 23:
            return w_53

  fastf_UnicodeTranslateError___init__ = __init__
  fastf_UnicodeTranslateError___init__.__name__ = 'fastf_UnicodeTranslateError___init__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__str__'
## firstlineno 155
##SECTION##
# global declarations
# global object gs_end
# global object gs_start
# global object gs_object
# global object gi_255
# global object gs_reason
# global object gs_can_t_translate_character_u___x_
# global object gi_65535
# global object gs_can_t_translate_character_u___u_
# global object gs_can_t_translate_character_u___U_
# global object gs_can_t_translate_characters_in_po

  def __str__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_end)
            w_1 = space.getattr(w_self, gs_start)
            w_2 = space.add(w_1, gi_1)
            w_3 = space.eq(w_0, w_2)
            v0 = space.is_true(w_3)
            if v0 == True:
                goto = 2
            else:
                goto = 7

        if goto == 2:
            w_4 = space.getattr(w_self, gs_object)
            w_5 = space.getattr(w_self, gs_start)
            w_6 = space.getitem(w_4, w_5)
            w_7 = space.ord(w_6)
            w_8 = space.le(w_7, gi_255)
            v1 = space.is_true(w_8)
            if v1 == True:
                goto = 3
            else:
                goto = 4

        if goto == 3:
            w_9 = space.getattr(w_self, gs_start)
            w_10 = space.getattr(w_self, gs_reason)
            w_11 = space.newtuple([w_7, w_9, w_10])
            w_12 = space.mod(gs_can_t_translate_character_u___x_, w_11)
            w_13 = w_12
            goto = 8

        if goto == 4:
            w_14 = space.le(w_7, gi_65535)
            v2 = space.is_true(w_14)
            if v2 == True:
                goto = 5
            else:
                goto = 6

        if goto == 5:
            w_15 = space.getattr(w_self, gs_start)
            w_16 = space.getattr(w_self, gs_reason)
            w_17 = space.newtuple([w_7, w_15, w_16])
            w_18 = space.mod(gs_can_t_translate_character_u___u_, w_17)
            w_13 = w_18
            goto = 8

        if goto == 6:
            w_19 = space.getattr(w_self, gs_start)
            w_20 = space.getattr(w_self, gs_reason)
            w_21 = space.newtuple([w_7, w_19, w_20])
            w_22 = space.mod(gs_can_t_translate_character_u___U_, w_21)
            w_13 = w_22
            goto = 8

        if goto == 7:
            w_23 = space.getattr(w_self, gs_start)
            w_24 = space.getattr(w_self, gs_end)
            w_25 = space.sub(w_24, gi_1)
            w_26 = space.getattr(w_self, gs_reason)
            w_27 = space.newtuple([w_23, w_25, w_26])
            w_28 = space.mod(gs_can_t_translate_characters_in_po, w_27)
            w_13 = w_28
            goto = 8

        if goto == 8:
            return w_13

  fastf_UnicodeTranslateError___str__ = __str__
  fastf_UnicodeTranslateError___str__.__name__ = 'fastf_UnicodeTranslateError___str__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__str__'
## firstlineno 171
##SECTION##
  def __str__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_args = space.getattr(w_self, gs_args)
            w_0 = space.len(w_args)
            w_1 = space.eq(w_0, gi_0)
            v0 = space.is_true(w_1)
            if v0 == True:
                w_2 = gs__emptystr_
                goto = 5
            else:
                goto = 2

        if goto == 2:
            w_3 = space.eq(w_0, gi_1)
            v1 = space.is_true(w_3)
            if v1 == True:
                goto = 3
            else:
                goto = 4

        if goto == 3:
            w_4 = space.getitem(w_args, gi_0)
            w_5 = space.repr(w_4)
            w_2 = w_5
            goto = 5

        if goto == 4:
            w_6 = space.str(w_args)
            w_2 = w_6
            goto = 5

        if goto == 5:
            return w_2

  fastf_KeyError___str__ = __str__
  fastf_KeyError___str__.__name__ = 'fastf_KeyError___str__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__init__'
## firstlineno 193
##SECTION##
  def __init__(space, __args__):
    funcname = "__init__"
    signature = ['self'], 'args', None
    defaults_w = []
    w_self, w_args = __args__.parse(funcname, signature, defaults_w)
    return fastf_EnvironmentError___init__(space, w_self, w_args)

  f_EnvironmentError___init__ = __init__
  f_EnvironmentError___init__.__name__ = 'f_EnvironmentError___init__'

  def __init__(space, w_self, w_args):
    goto = 1 # startblock
    while True:

        if goto == 1:
            _args = gateway.Arguments.fromshape(space, (1, [], True, False), [w_self, w_args])
            w_0 = space.call_args(gfunc_BaseException___init__, _args)
            w_argc = space.len(w_args)
            w_1 = space.setattr(w_self, gs_args, w_args)
            w_2 = space.setattr(w_self, gs_errno, space.w_None)
            w_3 = space.setattr(w_self, gs_strerror, space.w_None)
            w_4 = space.setattr(w_self, gs_filename, space.w_None)
            w_5 = space.le(gi_2, w_argc)
            v0 = space.is_true(w_5)
            if v0 == True:
                goto = 2
            else:
                goto = 5

        if goto == 2:
            w_6 = space.le(w_argc, gi_3)
            goto = 3

        if goto == 3:
            v1 = space.is_true(w_6)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 4:
            w_7 = space.getitem(w_args, gi_0)
            w_8 = space.setattr(w_self, gs_errno, w_7)
            w_9 = space.getitem(w_args, gi_1)
            w_10 = space.setattr(w_self, gs_strerror, w_9)
            goto = 5

        if goto == 5:
            w_11 = space.eq(w_argc, gi_3)
            v2 = space.is_true(w_11)
            if v2 == True:
                goto = 6
            else:
                w_12 = space.w_None
                goto = 7

        if goto == 6:
            w_13 = space.getitem(w_args, gi_2)
            w_14 = space.setattr(w_self, gs_filename, w_13)
            w_15 = space.getitem(w_args, gi_0)
            w_16 = space.getitem(w_args, gi_1)
            w_17 = space.newtuple([w_15, w_16])
            w_18 = space.setattr(w_self, gs_args, w_17)
            w_12 = space.w_None
            goto = 7

        if goto == 7:
            return w_12

  fastf_EnvironmentError___init__ = __init__
  fastf_EnvironmentError___init__.__name__ = 'fastf_EnvironmentError___init__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__str__'
## firstlineno 207
##SECTION##
# global declarations
# global object gs_errno
# global object gs_strerror
# global object gs__Errno__s___s___s
# global object gs__Errno__s___s

  def __str__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_filename)
            w_1 = space.is_(w_0, space.w_None)
            v0 = space.is_true(w_1)
            if v0 == True:
                goto = 3
            else:
                goto = 2

        if goto == 2:
            w_2 = space.getattr(w_self, gs_errno)
            w_3 = space.getattr(w_self, gs_strerror)
            w_4 = space.getattr(w_self, gs_filename)
            w_5 = space.newtuple([w_2, w_3, w_4])
            w_6 = space.mod(gs__Errno__s___s___s, w_5)
            w_7 = w_6
            goto = 7

        if goto == 3:
            w_8 = space.getattr(w_self, gs_errno)
            v1 = space.is_true(w_8)
            if v1 == True:
                goto = 4
            else:
                goto = 6

        if goto == 4:
            w_9 = space.getattr(w_self, gs_strerror)
            v2 = space.is_true(w_9)
            if v2 == True:
                goto = 5
            else:
                goto = 6

        if goto == 5:
            w_10 = space.getattr(w_self, gs_errno)
            w_11 = space.getattr(w_self, gs_strerror)
            w_12 = space.newtuple([w_10, w_11])
            w_13 = space.mod(gs__Errno__s___s, w_12)
            w_7 = w_13
            goto = 7

        if goto == 6:
            w_14 = fastf_BaseException___str__(space, w_self)
            w_7 = w_14
            goto = 7

        if goto == 7:
            return w_7

  fastf_EnvironmentError___str__ = __str__
  fastf_EnvironmentError___str__.__name__ = 'fastf_EnvironmentError___str__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__init__'
## firstlineno 283
##SECTION##
# global declarations
# global object gs_argument_1_must_be_str__not__s
# global object gs_argument_3_must_be_int__not__s
# global object gs_argument_4_must_be_str__not__s

  def __init__(space, __args__):
    funcname = "__init__"
    signature = ['self'], 'args', None
    defaults_w = []
    w_self, w_args = __args__.parse(funcname, signature, defaults_w)
    return fastf_SyntaxError___init__(space, w_self, w_args)

  f_SyntaxError___init__ = __init__
  f_SyntaxError___init__.__name__ = 'f_SyntaxError___init__'

  def __init__(space, w_self, w_args):
    goto = 1 # startblock
    while True:

        if goto == 1:
            _args = gateway.Arguments.fromshape(space, (1, [], True, False), [w_self, w_args])
            w_0 = space.call_args(gfunc_BaseException___init__, _args)
            w_argc = space.len(w_args)
            w_1 = space.setattr(w_self, gs_args, w_args)
            w_2 = space.ge(w_argc, gi_1)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_3 = space.getitem(w_args, gi_0)
            w_4 = space.setattr(w_self, gs_msg, w_3)
            goto = 3

        if goto == 3:
            w_5 = space.eq(w_argc, gi_2)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 4
            else:
                w_6 = space.w_None
                goto = 26

        if goto == 4:
            w_7 = space.getitem(w_args, gi_1)
            w_8 = space.getitem(w_7, gi_0)
            w_9 = space.is_(w_8, space.w_None)
            v2 = space.is_true(w_9)
            if v2 == True:
                goto = 6
            else:
                goto = 5

        if goto == 5:
            w_10 = space.getitem(w_args, gi_1)
            w_11 = space.getitem(w_10, gi_0)
            w_12 = space.type(w_11)
            w_13 = space.eq(w_12, space.w_str)
            v3 = space.is_true(w_13)
            if v3 == True:
                goto = 6
            else:
                goto = 7

        if goto == 6:
            w_14 = space.getitem(w_args, gi_1)
            w_15 = space.getitem(w_14, gi_0)
            w_16 = space.setattr(w_self, gs_filename, w_15)
            w_17 = space.getitem(w_args, gi_1)
            w_18 = space.getitem(w_17, gi_1)
            w_19 = space.is_(w_18, space.w_None)
            v4 = space.is_true(w_19)
            if v4 == True:
                goto = 10
            else:
                goto = 9

        if goto == 7:
            w_20 = space.getitem(w_args, gi_1)
            w_21 = space.getitem(w_20, gi_0)
            w_22 = space.type(w_21)
            w_23 = space.mod(gs_argument_1_must_be_str__not__s, w_22)
            w_24 = space.call_function(gcls_TypeError, w_23)
            w_25 = space.type(w_24)
            w_26 = space.issubtype(w_25, space.w_type)
            v5 = space.is_true(w_26)
            if v5 == True:
                goto = 8
            else:
                goto = 13

        if goto == 8:
            w_27 = space.call_function(w_24, )
            w_28 = space.type(w_27)
            w_etype, w_evalue = w_28, w_27
            goto = 25

        if goto == 9:
            w_29 = space.getitem(w_args, gi_1)
            w_30 = space.getitem(w_29, gi_1)
            w_31 = space.type(w_30)
            w_32 = space.eq(w_31, space.w_int)
            v6 = space.is_true(w_32)
            if v6 == True:
                goto = 10
            else:
                goto = 11

        if goto == 10:
            w_33 = space.getitem(w_args, gi_1)
            w_34 = space.getitem(w_33, gi_1)
            w_35 = space.setattr(w_self, gs_lineno, w_34)
            w_36 = space.getitem(w_args, gi_1)
            w_37 = space.getitem(w_36, gi_2)
            w_38 = space.is_(w_37, space.w_None)
            v7 = space.is_true(w_38)
            if v7 == True:
                goto = 15
            else:
                goto = 14

        if goto == 11:
            w_39 = space.getitem(w_args, gi_1)
            w_40 = space.getitem(w_39, gi_1)
            w_41 = space.type(w_40)
            w_42 = space.mod(gs_argument_2_must_be_int__not__s, w_41)
            w_43 = space.call_function(gcls_TypeError, w_42)
            w_44 = space.type(w_43)
            w_45 = space.issubtype(w_44, space.w_type)
            v8 = space.is_true(w_45)
            if v8 == True:
                goto = 12
            else:
                goto = 18

        if goto == 12:
            w_46 = space.call_function(w_43, )
            w_47 = space.type(w_46)
            w_etype, w_evalue = w_47, w_46
            goto = 25

        if goto == 13:
            w_48 = space.type(w_24)
            w_etype, w_evalue = w_48, w_24
            goto = 25

        if goto == 14:
            w_49 = space.getitem(w_args, gi_1)
            w_50 = space.getitem(w_49, gi_2)
            w_51 = space.type(w_50)
            w_52 = space.eq(w_51, space.w_int)
            v9 = space.is_true(w_52)
            if v9 == True:
                goto = 15
            else:
                goto = 16

        if goto == 15:
            w_53 = space.getitem(w_args, gi_1)
            w_54 = space.getitem(w_53, gi_2)
            w_55 = space.setattr(w_self, gs_offset, w_54)
            w_56 = space.getitem(w_args, gi_1)
            w_57 = space.getitem(w_56, gi_3)
            w_58 = space.is_(w_57, space.w_None)
            v10 = space.is_true(w_58)
            if v10 == True:
                goto = 21
            else:
                goto = 19

        if goto == 16:
            w_59 = space.getitem(w_args, gi_1)
            w_60 = space.getitem(w_59, gi_2)
            w_61 = space.type(w_60)
            w_62 = space.mod(gs_argument_3_must_be_int__not__s, w_61)
            w_63 = space.call_function(gcls_TypeError, w_62)
            w_64 = space.type(w_63)
            w_65 = space.issubtype(w_64, space.w_type)
            v11 = space.is_true(w_65)
            if v11 == True:
                goto = 17
            else:
                goto = 20

        if goto == 17:
            w_66 = space.call_function(w_63, )
            w_67 = space.type(w_66)
            w_etype, w_evalue = w_67, w_66
            goto = 25

        if goto == 18:
            w_68 = space.type(w_43)
            w_etype, w_evalue = w_68, w_43
            goto = 25

        if goto == 19:
            w_69 = space.getitem(w_args, gi_1)
            w_70 = space.getitem(w_69, gi_3)
            w_71 = space.type(w_70)
            w_72 = space.eq(w_71, space.w_str)
            v12 = space.is_true(w_72)
            if v12 == True:
                goto = 21
            else:
                goto = 22

        if goto == 20:
            w_73 = space.type(w_63)
            w_etype, w_evalue = w_73, w_63
            goto = 25

        if goto == 21:
            w_74 = space.getitem(w_args, gi_1)
            w_75 = space.getitem(w_74, gi_3)
            w_76 = space.setattr(w_self, gs_text, w_75)
            w_6 = space.w_None
            goto = 26

        if goto == 22:
            w_77 = space.getitem(w_args, gi_1)
            w_78 = space.getitem(w_77, gi_3)
            w_79 = space.type(w_78)
            w_80 = space.mod(gs_argument_4_must_be_str__not__s, w_79)
            w_81 = space.call_function(gcls_TypeError, w_80)
            w_82 = space.type(w_81)
            w_83 = space.issubtype(w_82, space.w_type)
            v13 = space.is_true(w_83)
            if v13 == True:
                goto = 24
            else:
                goto = 23

        if goto == 23:
            w_84 = space.type(w_81)
            w_etype, w_evalue = w_84, w_81
            goto = 25

        if goto == 24:
            w_85 = space.call_function(w_81, )
            w_86 = space.type(w_85)
            w_etype, w_evalue = w_86, w_85
            goto = 25

        if goto == 25:
            raise gOperationError(w_etype, w_evalue)

        if goto == 26:
            return w_6

  fastf_SyntaxError___init__ = __init__
  fastf_SyntaxError___init__.__name__ = 'fastf_SyntaxError___init__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__str__'
## firstlineno 307
##SECTION##
# global declarations
# global object gs___import__
# global object gs_os
# global object g0dict
# global object gs_path
# global object gs_basename
# global object gs____
# global object gs__s___s__line__ld_
# global object gs__s___s_
# global object gs__s__line__ld_

  def __str__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_msg)
            w_1 = space.type(w_0)
            w_2 = space.is_(w_1, space.w_str)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 3
            else:
                goto = 2

        if goto == 2:
            w_3 = space.getattr(w_self, gs_msg)
            w_4 = w_3
            goto = 13

        if goto == 3:
            w_buffer = space.getattr(w_self, gs_msg)
            w_5 = space.getattr(w_self, gs_filename)
            w_6 = space.type(w_5)
            w_have_filename = space.is_(w_6, space.w_str)
            w_7 = space.getattr(w_self, gs_lineno)
            w_8 = space.type(w_7)
            w_have_lineno = space.is_(w_8, space.w_int)
            v1 = space.is_true(w_have_filename)
            if v1 == True:
                goto = 5
            else:
                goto = 4

        if goto == 4:
            v2 = space.is_true(w_have_lineno)
            if v2 == True:
                goto = 5
            else:
                w_4 = w_buffer
                goto = 13

        if goto == 5:
            w_9 = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs_os, g0dict, space.w_None, space.w_None)
            w_10 = space.getattr(w_9, gs_path)
            w_11 = space.getattr(w_10, gs_basename)
            w_12 = space.getattr(w_self, gs_filename)
            v3 = space.is_true(w_12)
            if v3 == True:
                w_13 = w_12
                goto = 6
            else:
                w_13 = gs____
                goto = 6

        if goto == 6:
            w_fname = space.call_function(w_11, w_13)
            v4 = space.is_true(w_have_filename)
            if v4 == True:
                goto = 7
            else:
                goto = 11

        if goto == 7:
            v5 = space.is_true(w_have_lineno)
            if v5 == True:
                goto = 8
            else:
                goto = 9

        if goto == 8:
            w_14 = space.getattr(w_self, gs_msg)
            w_15 = space.getattr(w_self, gs_lineno)
            w_16 = space.newtuple([w_14, w_fname, w_15])
            w_17 = space.mod(gs__s___s__line__ld_, w_16)
            w_4 = w_17
            goto = 13

        if goto == 9:
            v6 = space.is_true(w_have_filename)
            if v6 == True:
                goto = 10
            else:
                goto = 11

        if goto == 10:
            w_18 = space.getattr(w_self, gs_msg)
            w_19 = space.newtuple([w_18, w_fname])
            w_20 = space.mod(gs__s___s_, w_19)
            w_4 = w_20
            goto = 13

        if goto == 11:
            v7 = space.is_true(w_have_lineno)
            if v7 == True:
                goto = 12
            else:
                w_4 = w_buffer
                goto = 13

        if goto == 12:
            w_21 = space.getattr(w_self, gs_msg)
            w_22 = space.getattr(w_self, gs_lineno)
            w_23 = space.newtuple([w_21, w_22])
            w_24 = space.mod(gs__s__line__ld_, w_23)
            w_4 = w_24
            goto = 13

        if goto == 13:
            return w_4

  fastf_SyntaxError___str__ = __str__
  fastf_SyntaxError___str__.__name__ = 'fastf_SyntaxError___str__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__init__'
## firstlineno 332
##SECTION##
# global declarations
# global object gs_code
# global object gs_argument_0_must_be_tuple__not__s

  def __init__(space, __args__):
    funcname = "__init__"
    signature = ['self'], 'args', None
    defaults_w = []
    w_self, w_1 = __args__.parse(funcname, signature, defaults_w)
    return fastf_SystemExit___init__(space, w_self, w_1)

  f_SystemExit___init__ = __init__
  f_SystemExit___init__.__name__ = 'f_SystemExit___init__'

  def __init__(space, w_self, w_1):
    goto = 1 # startblock
    while True:

        if goto == 1:
            _args = gateway.Arguments.fromshape(space, (1, [], True, False), [w_self, w_1])
            w_0 = space.call_args(gfunc_BaseException___init__, _args)
            w_argc = space.len(w_1)
            w_2 = space.eq(w_argc, gi_0)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_3 = space.setattr(w_self, gs_code, space.w_None)
            goto = 3

        if goto == 3:
            w_4 = space.setattr(w_self, gs_args, w_1)
            w_5 = space.eq(w_argc, gi_1)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 4:
            w_6 = space.getitem(w_1, gi_0)
            w_7 = space.setattr(w_self, gs_code, w_6)
            goto = 5

        if goto == 5:
            w_8 = space.ge(w_argc, gi_2)
            v2 = space.is_true(w_8)
            if v2 == True:
                goto = 6
            else:
                w_9 = space.w_None
                goto = 12

        if goto == 6:
            w_10 = space.type(w_1)
            w_11 = space.eq(w_10, space.w_tuple)
            v3 = space.is_true(w_11)
            if v3 == True:
                goto = 7
            else:
                goto = 8

        if goto == 7:
            w_12 = space.setattr(w_self, gs_code, w_1)
            w_9 = space.w_None
            goto = 12

        if goto == 8:
            w_13 = space.type(w_1)
            w_14 = space.mod(gs_argument_0_must_be_tuple__not__s, w_13)
            w_15 = space.call_function(gcls_TypeError, w_14)
            w_16 = space.type(w_15)
            w_17 = space.issubtype(w_16, space.w_type)
            v4 = space.is_true(w_17)
            if v4 == True:
                goto = 10
            else:
                goto = 9

        if goto == 9:
            w_18 = space.type(w_15)
            w_etype, w_evalue = w_18, w_15
            goto = 11

        if goto == 10:
            w_19 = space.call_function(w_15, )
            w_20 = space.type(w_19)
            w_etype, w_evalue = w_20, w_19
            goto = 11

        if goto == 11:
            raise gOperationError(w_etype, w_evalue)

        if goto == 12:
            return w_9

  fastf_SystemExit___init__ = __init__
  fastf_SystemExit___init__.__name__ = 'fastf_SystemExit___init__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__init__'
## firstlineno 370
##SECTION##
  def __init__(space, __args__):
    funcname = "__init__"
    signature = ['self'], 'args', None
    defaults_w = []
    w_self, w_args = __args__.parse(funcname, signature, defaults_w)
    return fastf_UnicodeDecodeError___init__(space, w_self, w_args)

  f_UnicodeDecodeError___init__ = __init__
  f_UnicodeDecodeError___init__.__name__ = 'f_UnicodeDecodeError___init__'

  def __init__(space, w_self, w_args):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_args)
            w_1 = space.setattr(w_self, gs_args, w_args)
            w_2 = space.eq(w_0, gi_5)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 2
            else:
                goto = 24

        if goto == 2:
            w_3 = space.getitem(w_args, gi_0)
            w_4 = space.type(w_3)
            w_5 = space.eq(w_4, space.w_str)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 3:
            w_6 = space.type(w_7)
            w_etype, w_evalue = w_6, w_7
            goto = 26

        if goto == 4:
            w_8 = space.getitem(w_args, gi_0)
            w_9 = space.setattr(w_self, gs_encoding, w_8)
            w_10 = space.getitem(w_args, gi_1)
            w_11 = space.type(w_10)
            w_12 = space.eq(w_11, space.w_str)
            v2 = space.is_true(w_12)
            if v2 == True:
                goto = 8
            else:
                goto = 9

        if goto == 5:
            w_13 = space.getitem(w_args, gi_0)
            w_14 = space.type(w_13)
            w_15 = space.mod(gs_argument_0_must_be_str__not__s, w_14)
            w_16 = space.call_function(gcls_TypeError, w_15)
            w_17 = space.type(w_16)
            w_18 = space.issubtype(w_17, space.w_type)
            v3 = space.is_true(w_18)
            if v3 == True:
                goto = 6
            else:
                goto = 7

        if goto == 6:
            w_19 = space.call_function(w_16, )
            w_20 = space.type(w_19)
            w_etype, w_evalue = w_20, w_19
            goto = 26

        if goto == 7:
            w_21 = space.type(w_16)
            w_etype, w_evalue = w_21, w_16
            goto = 26

        if goto == 8:
            w_22 = space.getitem(w_args, gi_1)
            w_23 = space.setattr(w_self, gs_object, w_22)
            w_24 = space.getitem(w_args, gi_2)
            w_25 = space.type(w_24)
            w_26 = space.eq(w_25, space.w_int)
            v4 = space.is_true(w_26)
            if v4 == True:
                goto = 12
            else:
                goto = 13

        if goto == 9:
            w_27 = space.getitem(w_args, gi_1)
            w_28 = space.type(w_27)
            w_29 = space.mod(gs_argument_1_must_be_str__not__s, w_28)
            w_30 = space.call_function(gcls_TypeError, w_29)
            w_31 = space.type(w_30)
            w_32 = space.issubtype(w_31, space.w_type)
            v5 = space.is_true(w_32)
            if v5 == True:
                goto = 10
            else:
                goto = 11

        if goto == 10:
            w_33 = space.call_function(w_30, )
            w_34 = space.type(w_33)
            w_etype, w_evalue = w_34, w_33
            goto = 26

        if goto == 11:
            w_35 = space.type(w_30)
            w_etype, w_evalue = w_35, w_30
            goto = 26

        if goto == 12:
            w_36 = space.getitem(w_args, gi_2)
            w_37 = space.setattr(w_self, gs_start, w_36)
            w_38 = space.getitem(w_args, gi_3)
            w_39 = space.type(w_38)
            w_40 = space.eq(w_39, space.w_int)
            v6 = space.is_true(w_40)
            if v6 == True:
                goto = 16
            else:
                goto = 17

        if goto == 13:
            w_41 = space.getitem(w_args, gi_2)
            w_42 = space.type(w_41)
            w_43 = space.mod(gs_argument_2_must_be_int__not__s, w_42)
            w_44 = space.call_function(gcls_TypeError, w_43)
            w_45 = space.type(w_44)
            w_46 = space.issubtype(w_45, space.w_type)
            v7 = space.is_true(w_46)
            if v7 == True:
                goto = 14
            else:
                goto = 15

        if goto == 14:
            w_47 = space.call_function(w_44, )
            w_48 = space.type(w_47)
            w_etype, w_evalue = w_48, w_47
            goto = 26

        if goto == 15:
            w_49 = space.type(w_44)
            w_etype, w_evalue = w_49, w_44
            goto = 26

        if goto == 16:
            w_50 = space.getitem(w_args, gi_3)
            w_51 = space.setattr(w_self, gs_end, w_50)
            w_52 = space.getitem(w_args, gi_4)
            w_53 = space.type(w_52)
            w_54 = space.eq(w_53, space.w_str)
            v8 = space.is_true(w_54)
            if v8 == True:
                goto = 20
            else:
                goto = 21

        if goto == 17:
            w_55 = space.getitem(w_args, gi_3)
            w_56 = space.type(w_55)
            w_57 = space.mod(gs_argument_3_must_be_int__not__s, w_56)
            w_58 = space.call_function(gcls_TypeError, w_57)
            w_59 = space.type(w_58)
            w_60 = space.issubtype(w_59, space.w_type)
            v9 = space.is_true(w_60)
            if v9 == True:
                goto = 18
            else:
                goto = 19

        if goto == 18:
            w_61 = space.call_function(w_58, )
            w_62 = space.type(w_61)
            w_etype, w_evalue = w_62, w_61
            goto = 26

        if goto == 19:
            w_63 = space.type(w_58)
            w_etype, w_evalue = w_63, w_58
            goto = 26

        if goto == 20:
            w_64 = space.getitem(w_args, gi_4)
            w_65 = space.setattr(w_self, gs_reason, w_64)
            w_66 = space.setattr(w_self, gs_message, gs__emptystr_)
            w_67 = space.w_None
            goto = 27

        if goto == 21:
            w_68 = space.getitem(w_args, gi_4)
            w_69 = space.type(w_68)
            w_70 = space.mod(gs_argument_4_must_be_str__not__s, w_69)
            w_71 = space.call_function(gcls_TypeError, w_70)
            w_72 = space.type(w_71)
            w_73 = space.issubtype(w_72, space.w_type)
            v10 = space.is_true(w_73)
            if v10 == True:
                goto = 23
            else:
                goto = 22

        if goto == 22:
            w_74 = space.type(w_71)
            w_etype, w_evalue = w_74, w_71
            goto = 26

        if goto == 23:
            w_75 = space.call_function(w_71, )
            w_76 = space.type(w_75)
            w_etype, w_evalue = w_76, w_75
            goto = 26

        if goto == 24:
            w_77 = space.mod(gs_function_takes_exactly_5_argumen, w_0)
            w_7 = space.call_function(gcls_TypeError, w_77)
            w_78 = space.type(w_7)
            w_79 = space.issubtype(w_78, space.w_type)
            v11 = space.is_true(w_79)
            if v11 == True:
                goto = 25
            else:
                goto = 3
                continue

        if goto == 25:
            w_80 = space.call_function(w_7, )
            w_81 = space.type(w_80)
            w_etype, w_evalue = w_81, w_80
            goto = 26

        if goto == 26:
            raise gOperationError(w_etype, w_evalue)

        if goto == 27:
            return w_67

  fastf_UnicodeDecodeError___init__ = __init__
  fastf_UnicodeDecodeError___init__.__name__ = 'fastf_UnicodeDecodeError___init__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__str__'
## firstlineno 398
##SECTION##
# global declarations
# global object gs__r_codec_can_t_decode_byte_0x_02
# global object gs__r_codec_can_t_decode_bytes_in_p

  def __str__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_end)
            w_1 = space.getattr(w_self, gs_start)
            w_2 = space.add(w_1, gi_1)
            w_3 = space.eq(w_0, w_2)
            v0 = space.is_true(w_3)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_4 = space.getattr(w_self, gs_encoding)
            w_5 = space.getattr(w_self, gs_object)
            w_6 = space.getattr(w_self, gs_start)
            w_7 = space.getitem(w_5, w_6)
            w_8 = space.ord(w_7)
            w_9 = space.getattr(w_self, gs_start)
            w_10 = space.getattr(w_self, gs_reason)
            w_11 = space.newtuple([w_4, w_8, w_9, w_10])
            w_12 = space.mod(gs__r_codec_can_t_decode_byte_0x_02, w_11)
            w_13 = w_12
            goto = 4

        if goto == 3:
            w_14 = space.getattr(w_self, gs_encoding)
            w_15 = space.getattr(w_self, gs_start)
            w_16 = space.getattr(w_self, gs_end)
            w_17 = space.sub(w_16, gi_1)
            w_18 = space.getattr(w_self, gs_reason)
            w_19 = space.newtuple([w_14, w_15, w_17, w_18])
            w_20 = space.mod(gs__r_codec_can_t_decode_bytes_in_p, w_19)
            w_13 = w_20
            goto = 4

        if goto == 4:
            return w_13

  fastf_UnicodeDecodeError___str__ = __str__
  fastf_UnicodeDecodeError___str__.__name__ = 'fastf_UnicodeDecodeError___str__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__init__'
## firstlineno 448
##SECTION##
# global declarations
# global object gi_5
# global object gs_argument_0_must_be_str__not__s
# global object gs_argument_1_must_be_unicode__not_
# global object gs_function_takes_exactly_5_argumen

  def __init__(space, __args__):
    funcname = "__init__"
    signature = ['self'], 'args', None
    defaults_w = []
    w_self, w_args = __args__.parse(funcname, signature, defaults_w)
    return fastf_UnicodeEncodeError___init__(space, w_self, w_args)

  f_UnicodeEncodeError___init__ = __init__
  f_UnicodeEncodeError___init__.__name__ = 'f_UnicodeEncodeError___init__'

  def __init__(space, w_self, w_args):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_args)
            w_1 = space.setattr(w_self, gs_args, w_args)
            w_2 = space.eq(w_0, gi_5)
            v0 = space.is_true(w_2)
            if v0 == True:
                goto = 2
            else:
                goto = 24

        if goto == 2:
            w_3 = space.getitem(w_args, gi_0)
            w_4 = space.type(w_3)
            w_5 = space.eq(w_4, space.w_str)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 3:
            w_6 = space.type(w_7)
            w_etype, w_evalue = w_6, w_7
            goto = 26

        if goto == 4:
            w_8 = space.getitem(w_args, gi_0)
            w_9 = space.setattr(w_self, gs_encoding, w_8)
            w_10 = space.getitem(w_args, gi_1)
            w_11 = space.type(w_10)
            w_12 = space.eq(w_11, space.w_unicode)
            v2 = space.is_true(w_12)
            if v2 == True:
                goto = 8
            else:
                goto = 9

        if goto == 5:
            w_13 = space.getitem(w_args, gi_0)
            w_14 = space.type(w_13)
            w_15 = space.mod(gs_argument_0_must_be_str__not__s, w_14)
            w_16 = space.call_function(gcls_TypeError, w_15)
            w_17 = space.type(w_16)
            w_18 = space.issubtype(w_17, space.w_type)
            v3 = space.is_true(w_18)
            if v3 == True:
                goto = 6
            else:
                goto = 7

        if goto == 6:
            w_19 = space.call_function(w_16, )
            w_20 = space.type(w_19)
            w_etype, w_evalue = w_20, w_19
            goto = 26

        if goto == 7:
            w_21 = space.type(w_16)
            w_etype, w_evalue = w_21, w_16
            goto = 26

        if goto == 8:
            w_22 = space.getitem(w_args, gi_1)
            w_23 = space.setattr(w_self, gs_object, w_22)
            w_24 = space.getitem(w_args, gi_2)
            w_25 = space.type(w_24)
            w_26 = space.eq(w_25, space.w_int)
            v4 = space.is_true(w_26)
            if v4 == True:
                goto = 12
            else:
                goto = 13

        if goto == 9:
            w_27 = space.getitem(w_args, gi_1)
            w_28 = space.type(w_27)
            w_29 = space.mod(gs_argument_1_must_be_unicode__not_, w_28)
            w_30 = space.call_function(gcls_TypeError, w_29)
            w_31 = space.type(w_30)
            w_32 = space.issubtype(w_31, space.w_type)
            v5 = space.is_true(w_32)
            if v5 == True:
                goto = 10
            else:
                goto = 11

        if goto == 10:
            w_33 = space.call_function(w_30, )
            w_34 = space.type(w_33)
            w_etype, w_evalue = w_34, w_33
            goto = 26

        if goto == 11:
            w_35 = space.type(w_30)
            w_etype, w_evalue = w_35, w_30
            goto = 26

        if goto == 12:
            w_36 = space.getitem(w_args, gi_2)
            w_37 = space.setattr(w_self, gs_start, w_36)
            w_38 = space.getitem(w_args, gi_3)
            w_39 = space.type(w_38)
            w_40 = space.eq(w_39, space.w_int)
            v6 = space.is_true(w_40)
            if v6 == True:
                goto = 16
            else:
                goto = 17

        if goto == 13:
            w_41 = space.getitem(w_args, gi_2)
            w_42 = space.type(w_41)
            w_43 = space.mod(gs_argument_2_must_be_int__not__s, w_42)
            w_44 = space.call_function(gcls_TypeError, w_43)
            w_45 = space.type(w_44)
            w_46 = space.issubtype(w_45, space.w_type)
            v7 = space.is_true(w_46)
            if v7 == True:
                goto = 14
            else:
                goto = 15

        if goto == 14:
            w_47 = space.call_function(w_44, )
            w_48 = space.type(w_47)
            w_etype, w_evalue = w_48, w_47
            goto = 26

        if goto == 15:
            w_49 = space.type(w_44)
            w_etype, w_evalue = w_49, w_44
            goto = 26

        if goto == 16:
            w_50 = space.getitem(w_args, gi_3)
            w_51 = space.setattr(w_self, gs_end, w_50)
            w_52 = space.getitem(w_args, gi_4)
            w_53 = space.type(w_52)
            w_54 = space.eq(w_53, space.w_str)
            v8 = space.is_true(w_54)
            if v8 == True:
                goto = 20
            else:
                goto = 21

        if goto == 17:
            w_55 = space.getitem(w_args, gi_3)
            w_56 = space.type(w_55)
            w_57 = space.mod(gs_argument_3_must_be_int__not__s, w_56)
            w_58 = space.call_function(gcls_TypeError, w_57)
            w_59 = space.type(w_58)
            w_60 = space.issubtype(w_59, space.w_type)
            v9 = space.is_true(w_60)
            if v9 == True:
                goto = 18
            else:
                goto = 19

        if goto == 18:
            w_61 = space.call_function(w_58, )
            w_62 = space.type(w_61)
            w_etype, w_evalue = w_62, w_61
            goto = 26

        if goto == 19:
            w_63 = space.type(w_58)
            w_etype, w_evalue = w_63, w_58
            goto = 26

        if goto == 20:
            w_64 = space.getitem(w_args, gi_4)
            w_65 = space.setattr(w_self, gs_reason, w_64)
            w_66 = space.setattr(w_self, gs_message, gs__emptystr_)
            w_67 = space.w_None
            goto = 27

        if goto == 21:
            w_68 = space.getitem(w_args, gi_4)
            w_69 = space.type(w_68)
            w_70 = space.mod(gs_argument_4_must_be_str__not__s, w_69)
            w_71 = space.call_function(gcls_TypeError, w_70)
            w_72 = space.type(w_71)
            w_73 = space.issubtype(w_72, space.w_type)
            v10 = space.is_true(w_73)
            if v10 == True:
                goto = 23
            else:
                goto = 22

        if goto == 22:
            w_74 = space.type(w_71)
            w_etype, w_evalue = w_74, w_71
            goto = 26

        if goto == 23:
            w_75 = space.call_function(w_71, )
            w_76 = space.type(w_75)
            w_etype, w_evalue = w_76, w_75
            goto = 26

        if goto == 24:
            w_77 = space.mod(gs_function_takes_exactly_5_argumen, w_0)
            w_7 = space.call_function(gcls_TypeError, w_77)
            w_78 = space.type(w_7)
            w_79 = space.issubtype(w_78, space.w_type)
            v11 = space.is_true(w_79)
            if v11 == True:
                goto = 25
            else:
                goto = 3
                continue

        if goto == 25:
            w_80 = space.call_function(w_7, )
            w_81 = space.type(w_80)
            w_etype, w_evalue = w_81, w_80
            goto = 26

        if goto == 26:
            raise gOperationError(w_etype, w_evalue)

        if goto == 27:
            return w_67

  fastf_UnicodeEncodeError___init__ = __init__
  fastf_UnicodeEncodeError___init__.__name__ = 'fastf_UnicodeEncodeError___init__'

##SECTION##
## filename    'lib/_exceptions.py'
## function    '__str__'
## firstlineno 476
##SECTION##
# global declarations
# global object gs_encoding
# global object gs__r_codec_can_t_encode_character_
# global object gs__r_codec_can_t_encode_character__1
# global object gs__r_codec_can_t_encode_character__2
# global object gs__r_codec_can_t_encode_characters

  def __str__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_end)
            w_1 = space.getattr(w_self, gs_start)
            w_2 = space.add(w_1, gi_1)
            w_3 = space.eq(w_0, w_2)
            v0 = space.is_true(w_3)
            if v0 == True:
                goto = 2
            else:
                goto = 7

        if goto == 2:
            w_4 = space.getattr(w_self, gs_object)
            w_5 = space.getattr(w_self, gs_start)
            w_6 = space.getitem(w_4, w_5)
            w_badchar = space.ord(w_6)
            w_7 = space.le(w_badchar, gi_255)
            v1 = space.is_true(w_7)
            if v1 == True:
                goto = 3
            else:
                goto = 4

        if goto == 3:
            w_8 = space.getattr(w_self, gs_encoding)
            w_9 = space.getattr(w_self, gs_start)
            w_10 = space.getattr(w_self, gs_reason)
            w_11 = space.newtuple([w_8, w_badchar, w_9, w_10])
            w_12 = space.mod(gs__r_codec_can_t_encode_character_, w_11)
            w_13 = w_12
            goto = 8

        if goto == 4:
            w_14 = space.le(w_badchar, gi_65535)
            v2 = space.is_true(w_14)
            if v2 == True:
                goto = 5
            else:
                goto = 6

        if goto == 5:
            w_15 = space.getattr(w_self, gs_encoding)
            w_16 = space.getattr(w_self, gs_start)
            w_17 = space.getattr(w_self, gs_reason)
            w_18 = space.newtuple([w_15, w_badchar, w_16, w_17])
            w_19 = space.mod(gs__r_codec_can_t_encode_character__1, w_18)
            w_13 = w_19
            goto = 8

        if goto == 6:
            w_20 = space.getattr(w_self, gs_encoding)
            w_21 = space.getattr(w_self, gs_start)
            w_22 = space.getattr(w_self, gs_reason)
            w_23 = space.newtuple([w_20, w_badchar, w_21, w_22])
            w_24 = space.mod(gs__r_codec_can_t_encode_character__2, w_23)
            w_13 = w_24
            goto = 8

        if goto == 7:
            w_25 = space.getattr(w_self, gs_encoding)
            w_26 = space.getattr(w_self, gs_start)
            w_27 = space.getattr(w_self, gs_end)
            w_28 = space.sub(w_27, gi_1)
            w_29 = space.getattr(w_self, gs_reason)
            w_30 = space.newtuple([w_25, w_26, w_28, w_29])
            w_31 = space.mod(gs__r_codec_can_t_encode_characters, w_30)
            w_13 = w_31
            goto = 8

        if goto == 8:
            return w_13

  fastf_UnicodeEncodeError___str__ = __str__
  fastf_UnicodeEncodeError___str__.__name__ = 'fastf_UnicodeEncodeError___str__'

##SECTION##
  w__doc__ = space.new_interned_str(__doc__)
  g50dict = space.newdict()
  gs_GeneratorExit = space.new_interned_str('GeneratorExit')
  gs___module__ = space.new_interned_str('__module__')
  gs_exceptions = space.new_interned_str('exceptions')
  gs___doc__ = space.new_interned_str('__doc__')
  gs_BaseException = space.new_interned_str('BaseException')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Superclass representing the base of the exception hierarchy.

    The __getitem__ method is provided for backwards-compatibility
    and will be deprecated at some point. 
    """)
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([space.w_object])
  _args = space.newtuple([gs_BaseException, _bases, _dic])
  gcls_BaseException = space.call(space.w_type, _args)
  gs_Exception = space.new_interned_str('Exception')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Common base class for all non-exit exceptions.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_BaseException])
  _args = space.newtuple([gs_Exception, _bases, _dic])
  gcls_Exception = space.call(space.w_type, _args)
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Request that a generator exit.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Exception])
  _args = space.newtuple([gs_GeneratorExit, _bases, _dic])
  gcls_GeneratorExit = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_GeneratorExit, gcls_GeneratorExit)
  gs_ImportError = space.new_interned_str('ImportError')
  gs_StandardError = space.new_interned_str('StandardError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for all standard Python exceptions.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Exception])
  _args = space.newtuple([gs_StandardError, _bases, _dic])
  gcls_StandardError = space.call(space.w_type, _args)
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Import can't find module, or can't find name in module.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_ImportError, _bases, _dic])
  gcls_ImportError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_ImportError, gcls_ImportError)
  gs_RuntimeError = space.new_interned_str('RuntimeError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Unspecified run-time error.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_RuntimeError, _bases, _dic])
  gcls_RuntimeError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_RuntimeError, gcls_RuntimeError)
  gs_UnicodeTranslateError = space.new_interned_str('UnicodeTranslateError')
  gs_ValueError = space.new_interned_str('ValueError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Inappropriate argument value (of correct type).""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_ValueError, _bases, _dic])
  gcls_ValueError = space.call(space.w_type, _args)
  gs_UnicodeError = space.new_interned_str('UnicodeError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Unicode related error.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_ValueError])
  _args = space.newtuple([gs_UnicodeError, _bases, _dic])
  gcls_UnicodeError = space.call(space.w_type, _args)
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Unicode translation error.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_UnicodeError])
  _args = space.newtuple([gs_UnicodeTranslateError, _bases, _dic])
  gcls_UnicodeTranslateError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_UnicodeTranslateError, gcls_UnicodeTranslateError)
  gs_KeyError = space.new_interned_str('KeyError')
  gs_LookupError = space.new_interned_str('LookupError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for lookup errors.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_LookupError, _bases, _dic])
  gcls_LookupError = space.call(space.w_type, _args)
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Mapping key not found.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_LookupError])
  _args = space.newtuple([gs_KeyError, _bases, _dic])
  gcls_KeyError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_KeyError, gcls_KeyError)
  gs_SyntaxWarning = space.new_interned_str('SyntaxWarning')
  gs_Warning = space.new_interned_str('Warning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warning categories.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Exception])
  _args = space.newtuple([gs_Warning, _bases, _dic])
  gcls_Warning = space.call(space.w_type, _args)
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings about dubious syntax.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_SyntaxWarning, _bases, _dic])
  gcls_SyntaxWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_SyntaxWarning, gcls_SyntaxWarning)
  gs_StopIteration = space.new_interned_str('StopIteration')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Signal the end from iterator.next().""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Exception])
  _args = space.newtuple([gs_StopIteration, _bases, _dic])
  gcls_StopIteration = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_StopIteration, gcls_StopIteration)
  gs_PendingDeprecationWarning = space.new_interned_str('PendingDeprecationWarning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings about features which will be deprecated in the future.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_PendingDeprecationWarning, _bases, _dic])
  gcls_PendingDeprecationWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_PendingDeprecationWarning, gcls_PendingDeprecationWarning)
  gs_EnvironmentError = space.new_interned_str('EnvironmentError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for I/O related errors.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_EnvironmentError, _bases, _dic])
  gcls_EnvironmentError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_EnvironmentError, gcls_EnvironmentError)
  space.setitem(g50dict, gs_LookupError, gcls_LookupError)
  gs_OSError = space.new_interned_str('OSError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""OS system call failed.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_EnvironmentError])
  _args = space.newtuple([gs_OSError, _bases, _dic])
  gcls_OSError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_OSError, gcls_OSError)
  gs_DeprecationWarning = space.new_interned_str('DeprecationWarning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings about deprecated features.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_DeprecationWarning, _bases, _dic])
  gcls_DeprecationWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_DeprecationWarning, gcls_DeprecationWarning)
  space.setitem(g50dict, gs_UnicodeError, gcls_UnicodeError)
  gs_FloatingPointError = space.new_interned_str('FloatingPointError')
  gs_ArithmeticError = space.new_interned_str('ArithmeticError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for arithmetic errors.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_ArithmeticError, _bases, _dic])
  gcls_ArithmeticError = space.call(space.w_type, _args)
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Floating point operation failed.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_ArithmeticError])
  _args = space.newtuple([gs_FloatingPointError, _bases, _dic])
  gcls_FloatingPointError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_FloatingPointError, gcls_FloatingPointError)
  gs_UnicodeWarning = space.new_interned_str('UnicodeWarning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings about Unicode related problems, mostly
    related to conversion problems.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_UnicodeWarning, _bases, _dic])
  gcls_UnicodeWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_UnicodeWarning, gcls_UnicodeWarning)
  gs_AttributeError = space.new_interned_str('AttributeError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Attribute not found.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_AttributeError, _bases, _dic])
  gcls_AttributeError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_AttributeError, gcls_AttributeError)
  gs_IndentationError = space.new_interned_str('IndentationError')
  gs_SyntaxError = space.new_interned_str('SyntaxError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Invalid syntax.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_SyntaxError, _bases, _dic])
  gcls_SyntaxError = space.call(space.w_type, _args)
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Improper indentation.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_SyntaxError])
  _args = space.newtuple([gs_IndentationError, _bases, _dic])
  gcls_IndentationError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_IndentationError, gcls_IndentationError)
  gs_NameError = space.new_interned_str('NameError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Name not found globally.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_NameError, _bases, _dic])
  gcls_NameError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_NameError, gcls_NameError)
  gs_IOError = space.new_interned_str('IOError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""I/O operation failed.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_EnvironmentError])
  _args = space.newtuple([gs_IOError, _bases, _dic])
  gcls_IOError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_IOError, gcls_IOError)
  space.setitem(g50dict, gs_ValueError, gcls_ValueError)
  gs_FutureWarning = space.new_interned_str('FutureWarning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings about constructs that will change semantically in the future.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_FutureWarning, _bases, _dic])
  gcls_FutureWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_FutureWarning, gcls_FutureWarning)
  gs_ImportWarning = space.new_interned_str('ImportWarning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings about probable mistakes in module imports""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_ImportWarning, _bases, _dic])
  gcls_ImportWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_ImportWarning, gcls_ImportWarning)
  gs_SystemExit = space.new_interned_str('SystemExit')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Request to exit from the interpreter.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_BaseException])
  _args = space.newtuple([gs_SystemExit, _bases, _dic])
  gcls_SystemExit = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_SystemExit, gcls_SystemExit)
  space.setitem(g50dict, gs_Exception, gcls_Exception)
  gs_EOFError = space.new_interned_str('EOFError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Read beyond end of file.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_EOFError, _bases, _dic])
  gcls_EOFError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_EOFError, gcls_EOFError)
  space.setitem(g50dict, gs_StandardError, gcls_StandardError)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/lib/_exceptions.py""")
  space.setitem(g50dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_TabError = space.new_interned_str('TabError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Improper mixture of spaces and tabs.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_IndentationError])
  _args = space.newtuple([gs_TabError, _bases, _dic])
  gcls_TabError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_TabError, gcls_TabError)
  space.setitem(g50dict, gs_SyntaxError, gcls_SyntaxError)
  gs_UnicodeEncodeError = space.new_interned_str('UnicodeEncodeError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Unicode encoding error.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_UnicodeError])
  _args = space.newtuple([gs_UnicodeEncodeError, _bases, _dic])
  gcls_UnicodeEncodeError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_UnicodeEncodeError, gcls_UnicodeEncodeError)
  gs_UnboundLocalError = space.new_interned_str('UnboundLocalError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Local name referenced but not bound to a value.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_NameError])
  _args = space.newtuple([gs_UnboundLocalError, _bases, _dic])
  gcls_UnboundLocalError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_UnboundLocalError, gcls_UnboundLocalError)
  gs___name__ = space.new_interned_str('__name__')
  space.setitem(g50dict, gs___name__, gs_exceptions)
  gs_ReferenceError = space.new_interned_str('ReferenceError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Weak ref proxy used after referent went away.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_ReferenceError, _bases, _dic])
  gcls_ReferenceError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_ReferenceError, gcls_ReferenceError)
  gs_AssertionError = space.new_interned_str('AssertionError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Assertion failed.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_AssertionError, _bases, _dic])
  gcls_AssertionError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_AssertionError, gcls_AssertionError)
  gs_UnicodeDecodeError = space.new_interned_str('UnicodeDecodeError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Unicode decoding error.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_UnicodeError])
  _args = space.newtuple([gs_UnicodeDecodeError, _bases, _dic])
  gcls_UnicodeDecodeError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_UnicodeDecodeError, gcls_UnicodeDecodeError)
  gs_TypeError = space.new_interned_str('TypeError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Inappropriate argument type.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_TypeError, _bases, _dic])
  gcls_TypeError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_TypeError, gcls_TypeError)
  gs_IndexError = space.new_interned_str('IndexError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Sequence index out of range.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_LookupError])
  _args = space.newtuple([gs_IndexError, _bases, _dic])
  gcls_IndexError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_IndexError, gcls_IndexError)
  gs_RuntimeWarning = space.new_interned_str('RuntimeWarning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings about dubious runtime behavior.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_RuntimeWarning, _bases, _dic])
  gcls_RuntimeWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_RuntimeWarning, gcls_RuntimeWarning)
  gs_KeyboardInterrupt = space.new_interned_str('KeyboardInterrupt')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Program interrupted by user.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_BaseException])
  _args = space.newtuple([gs_KeyboardInterrupt, _bases, _dic])
  gcls_KeyboardInterrupt = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_KeyboardInterrupt, gcls_KeyboardInterrupt)
  gs_UserWarning = space.new_interned_str('UserWarning')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Base class for warnings generated by user code.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_Warning])
  _args = space.newtuple([gs_UserWarning, _bases, _dic])
  gcls_UserWarning = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_UserWarning, gcls_UserWarning)
  gs_ZeroDivisionError = space.new_interned_str('ZeroDivisionError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Second argument to a division or modulo operation was zero.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_ArithmeticError])
  _args = space.newtuple([gs_ZeroDivisionError, _bases, _dic])
  gcls_ZeroDivisionError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_ZeroDivisionError, gcls_ZeroDivisionError)
  gs_MemoryError = space.new_interned_str('MemoryError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Out of memory.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_MemoryError, _bases, _dic])
  gcls_MemoryError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_MemoryError, gcls_MemoryError)
  space.setitem(g50dict, gs___doc__, w__doc__)
  space.setitem(g50dict, gs_ArithmeticError, gcls_ArithmeticError)
  space.setitem(g50dict, gs_Warning, gcls_Warning)
  gs_NotImplementedError = space.new_interned_str('NotImplementedError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Method or function hasn't been implemented yet.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_RuntimeError])
  _args = space.newtuple([gs_NotImplementedError, _bases, _dic])
  gcls_NotImplementedError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_NotImplementedError, gcls_NotImplementedError)
  gs_SystemError = space.new_interned_str('SystemError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Internal error in the Python interpreter.

Please report this to the Python maintainer, along with the traceback,
the Python version, and the hardware/OS platform and version.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_StandardError])
  _args = space.newtuple([gs_SystemError, _bases, _dic])
  gcls_SystemError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_SystemError, gcls_SystemError)
  gs_OverflowError = space.new_interned_str('OverflowError')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs_exceptions)
  _doc = space.wrap("""Result too large to be represented.""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([gcls_ArithmeticError])
  _args = space.newtuple([gs_OverflowError, _bases, _dic])
  gcls_OverflowError = space.call(space.w_type, _args)
  space.setitem(g50dict, gs_OverflowError, gcls_OverflowError)
  space.setitem(g50dict, gs_BaseException, gcls_BaseException)
  gs___init__ = space.new_interned_str('__init__')
  from pypy.interpreter import gateway
  gfunc_UnicodeDecodeError___init__ = space.wrap(gateway.interp2app(f_UnicodeDecodeError___init__, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setattr(gcls_UnicodeDecodeError, gs___init__, gfunc_UnicodeDecodeError___init__)
  gs___str__ = space.new_interned_str('__str__')
  gfunc_UnicodeDecodeError___str__ = space.wrap(gateway.interp2app(fastf_UnicodeDecodeError___str__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_UnicodeDecodeError, gs___str__, gfunc_UnicodeDecodeError___str__)
  gfunc_UnicodeEncodeError___init__ = space.wrap(gateway.interp2app(f_UnicodeEncodeError___init__, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setattr(gcls_UnicodeEncodeError, gs___init__, gfunc_UnicodeEncodeError___init__)
  gfunc_UnicodeEncodeError___str__ = space.wrap(gateway.interp2app(fastf_UnicodeEncodeError___str__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_UnicodeEncodeError, gs___str__, gfunc_UnicodeEncodeError___str__)
  gfunc_SystemExit___init__ = space.wrap(gateway.interp2app(f_SystemExit___init__, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setattr(gcls_SystemExit, gs___init__, gfunc_SystemExit___init__)
  gfunc_SyntaxError___init__ = space.wrap(gateway.interp2app(f_SyntaxError___init__, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setattr(gcls_SyntaxError, gs___init__, gfunc_SyntaxError___init__)
  gfunc_SyntaxError___str__ = space.wrap(gateway.interp2app(fastf_SyntaxError___str__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_SyntaxError, gs___str__, gfunc_SyntaxError___str__)
  gs_filename = space.new_interned_str('filename')
  space.setattr(gcls_SyntaxError, gs_filename, space.w_None)
  gs_lineno = space.new_interned_str('lineno')
  space.setattr(gcls_SyntaxError, gs_lineno, space.w_None)
  gs_msg = space.new_interned_str('msg')
  gs__emptystr_ = space.new_interned_str('')
  space.setattr(gcls_SyntaxError, gs_msg, gs__emptystr_)
  gs_offset = space.new_interned_str('offset')
  space.setattr(gcls_SyntaxError, gs_offset, space.w_None)
  gs_print_file_and_line = space.new_interned_str('print_file_and_line')
  space.setattr(gcls_SyntaxError, gs_print_file_and_line, space.w_None)
  gs_text = space.new_interned_str('text')
  space.setattr(gcls_SyntaxError, gs_text, space.w_None)
  gfunc_EnvironmentError___init__ = space.wrap(gateway.interp2app(f_EnvironmentError___init__, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setattr(gcls_EnvironmentError, gs___init__, gfunc_EnvironmentError___init__)
  gfunc_EnvironmentError___str__ = space.wrap(gateway.interp2app(fastf_EnvironmentError___str__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_EnvironmentError, gs___str__, gfunc_EnvironmentError___str__)
  gfunc_KeyError___str__ = space.wrap(gateway.interp2app(fastf_KeyError___str__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_KeyError, gs___str__, gfunc_KeyError___str__)
  gfunc_UnicodeTranslateError___init__ = space.wrap(gateway.interp2app(f_UnicodeTranslateError___init__, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setattr(gcls_UnicodeTranslateError, gs___init__, gfunc_UnicodeTranslateError___init__)
  gfunc_UnicodeTranslateError___str__ = space.wrap(gateway.interp2app(fastf_UnicodeTranslateError___str__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_UnicodeTranslateError, gs___str__, gfunc_UnicodeTranslateError___str__)
  gs___getitem__ = space.new_interned_str('__getitem__')
  gfunc_BaseException___getitem__ = space.wrap(gateway.interp2app(fastf_BaseException___getitem__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setattr(gcls_BaseException, gs___getitem__, gfunc_BaseException___getitem__)
  gfunc_BaseException___init__ = space.wrap(gateway.interp2app(f_BaseException___init__, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setattr(gcls_BaseException, gs___init__, gfunc_BaseException___init__)
  gs___repr__ = space.new_interned_str('__repr__')
  gfunc_BaseException___repr__ = space.wrap(gateway.interp2app(fastf_BaseException___repr__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_BaseException, gs___repr__, gfunc_BaseException___repr__)
  gfunc_BaseException___str__ = space.wrap(gateway.interp2app(fastf_BaseException___str__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_BaseException, gs___str__, gfunc_BaseException___str__)
  gs_args = space.new_interned_str('args')
  gi_0 = space.wrap(0)
  gi_1 = space.wrap(1)
  gs___ = space.new_interned_str('()')
  gs___class__ = space.new_interned_str('__class__')
  gs_message = space.new_interned_str('message')
  gs_end = space.new_interned_str('end')
  gs_start = space.new_interned_str('start')
  gs_object = space.new_interned_str('object')
  gi_255 = space.wrap(255)
  gs_reason = space.new_interned_str('reason')
  gs_can_t_translate_character_u___x_ = space.new_interned_str(
"""can't translate character u'\\x%02x' in position %d: %s""")
  gi_65535 = space.wrap(65535)
  gs_can_t_translate_character_u___u_ = space.new_interned_str(
"""can't translate character u'\\u%04x' in position %d: %s""")
  gs_can_t_translate_character_u___U_ = space.new_interned_str(
"""can't translate character u'\\U%08x' in position %d: %s""")
  gs_can_t_translate_characters_in_po = space.new_interned_str(
"""can't translate characters in position %d-%d: %s""")
  gi_4 = space.wrap(4)
  gs_argument_0_must_be_unicode__not_ = space.new_interned_str(
"""argument 0 must be unicode, not %s""")
  gi_2 = space.wrap(2)
  gs_argument_1_must_be_int__not__s = space.new_interned_str(
"""argument 1 must be int, not %s""")
  gi_3 = space.wrap(3)
  gs_argument_2_must_be_int__not__s = space.new_interned_str(
"""argument 2 must be int, not %s""")
  gs_argument_3_must_be_str__not__s = space.new_interned_str(
"""argument 3 must be str, not %s""")
  gs_function_takes_exactly_4_argumen = space.new_interned_str(
"""function takes exactly 4 arguments (%d given)""")
  from pypy.interpreter.error import OperationError as gOperationError
  gs_errno = space.new_interned_str('errno')
  gs_strerror = space.new_interned_str('strerror')
  gs__Errno__s___s___s = space.new_interned_str('[Errno %s] %s: %s')
  gs__Errno__s___s = space.new_interned_str('[Errno %s] %s')
  gs___import__ = space.new_interned_str('__import__')
  gs_os = space.new_interned_str('os')
  g0dict = space.newdict()
  gs_path = space.new_interned_str('path')
  gs_basename = space.new_interned_str('basename')
  gs____ = space.new_interned_str('???')
  gs__s___s__line__ld_ = space.new_interned_str('%s (%s, line %ld)')
  gs__s___s_ = space.new_interned_str('%s (%s)')
  gs__s__line__ld_ = space.new_interned_str('%s (line %ld)')
  gs_argument_1_must_be_str__not__s = space.new_interned_str(
"""argument 1 must be str, not %s""")
  gs_argument_3_must_be_int__not__s = space.new_interned_str(
"""argument 3 must be int, not %s""")
  gs_argument_4_must_be_str__not__s = space.new_interned_str(
"""argument 4 must be str, not %s""")
  gs_code = space.new_interned_str('code')
  gs_argument_0_must_be_tuple__not__s = space.new_interned_str(
"""argument 0 must be tuple, not %s""")
  gs_encoding = space.new_interned_str('encoding')
  gs__r_codec_can_t_encode_character_ = space.new_interned_str(
"""%r codec can't encode character u'\\x%02x' in position %d: %s""")
  gs__r_codec_can_t_encode_character__1 = space.new_interned_str(
"""%r codec can't encode character u'\\u%04x' in position %d: %s""")
  gs__r_codec_can_t_encode_character__2 = space.new_interned_str(
"""%r codec can't encode character u'\\U%08x' in position %d: %s""")
  gs__r_codec_can_t_encode_characters = space.new_interned_str(
"""%r codec can't encode characters in position %d-%d: %s""")
  gi_5 = space.wrap(5)
  gs_argument_0_must_be_str__not__s = space.new_interned_str(
"""argument 0 must be str, not %s""")
  gs_argument_1_must_be_unicode__not_ = space.new_interned_str(
"""argument 1 must be unicode, not %s""")
  gs_function_takes_exactly_5_argumen = space.new_interned_str(
"""function takes exactly 5 arguments (%d given)""")
  gs__r_codec_can_t_decode_byte_0x_02 = space.new_interned_str(
"""%r codec can't decode byte 0x%02x in position %d: %s""")
  gs__r_codec_can_t_decode_bytes_in_p = space.new_interned_str(
"""%r codec can't decode bytes in position %d-%d: %s""")
  return g50dict


from pypy._cache import known_code
known_code['79773bc75ab921298d30069185ff81ee'] = initexceptions
