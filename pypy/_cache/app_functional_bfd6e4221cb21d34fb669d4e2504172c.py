# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'app_functional_bfd6e4221cb21d34fb669d4e2504172c')
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
Plain Python definition of the builtin functions oriented towards
functional programming.
"""

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'sum'
## firstlineno 8
##SECTION##
  def sum(space, __args__):
    """sum(sequence, start=0) -> value

Returns the sum of a sequence of numbers (NOT strings) plus the value
of parameter 'start'.  When the sequence is empty, returns start."""

    funcname = "sum"
    signature = ['sequence', 'total'], None, None
    defaults_w = [gi_0]
    w_1, w_total = __args__.parse(funcname, signature, defaults_w)
    return fastf_sum(space, w_1, w_total)

  f_sum = sum
  f_sum.__name__ = 'f_sum'

  def sum(space, w_1, w_total):
    """sum(sequence, start=0) -> value

Returns the sum of a sequence of numbers (NOT strings) plus the value
of parameter 'start'.  When the sequence is empty, returns start."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.isinstance(w_total, space.w_str)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_evalue = space.call_function(space.w_TypeError, )
            w_etype = space.type(w_evalue)
            goto = 6

        if goto == 3:
            w_2 = space.iter(w_1)
            w_3 = w_total
            goto = 4

        if goto == 4:
            try:
                w_4 = space.next(w_2)
                goto = 5
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 7
                else:raise # unhandled case, should not happen

        if goto == 5:
            w_5 = space.add(w_3, w_4)
            w_3 = w_5
            goto = 4
            continue

        if goto == 6:
            raise gOperationError(w_etype, w_evalue)

        if goto == 7:
            return w_3

  fastf_sum = sum
  fastf_sum.__name__ = 'fastf_sum'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'apply'
## firstlineno 21
##SECTION##
# global declarations
# global object g0tuple
# global object g0dict_3

  def apply(space, __args__):
    """call a function (or other callable object) and return its result"""

    funcname = "apply"
    signature = ['function', 'args', 'kwds'], None, None
    defaults_w = [g0tuple, g0dict_3]
    w_function, w_args, w_kwds = __args__.parse(funcname, signature, defaults_w)
    return fastf_apply(space, w_function, w_args, w_kwds)

  f_apply = apply
  f_apply.__name__ = 'f_apply'

  def apply(space, w_function, w_args, w_kwds):
    """call a function (or other callable object) and return its result"""
    goto = 1 # startblock
    while True:

        if goto == 1:
            _args = gateway.Arguments.fromshape(space, (0, [], True, True), [w_args, w_kwds])
            w_0 = space.call_args(w_function, _args)
            goto = 2

        if goto == 2:
            return w_0

  fastf_apply = apply
  fastf_apply.__name__ = 'fastf_apply'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'map'
## firstlineno 25
##SECTION##
# global declaration
# global object gs_map___requires_at_least_one_sequ

  def map(space, __args__):
    """does 3 separate things, hence this enormous docstring.
       1.  if function is None, return a list of tuples, each with one
           item from each collection.  If the collections have different
           lengths,  shorter ones are padded with None.

       2.  if function is not None, and there is only one collection,
           apply function to every item in the collection and return a
           list of the results.

       3.  if function is not None, and there are several collections,
           repeatedly call the function with one argument from each
           collection.  If the collections have different lengths,
           shorter ones are padded with None
    """

    funcname = "map"
    signature = ['function'], 'collections', None
    defaults_w = []
    w_function, w_collections = __args__.parse(funcname, signature, defaults_w)
    return fastf_map(space, w_function, w_collections)

  f_map = map
  f_map.__name__ = 'f_map'

  def map(space, w_function, w_collections):
    """does 3 separate things, hence this enormous docstring.
       1.  if function is None, return a list of tuples, each with one
           item from each collection.  If the collections have different
           lengths,  shorter ones are padded with None.

       2.  if function is not None, and there is only one collection,
           apply function to every item in the collection and return a
           list of the results.

       3.  if function is not None, and there are several collections,
           repeatedly call the function with one argument from each
           collection.  If the collections have different lengths,
           shorter ones are padded with None
    """
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_collections)
            w_1 = space.eq(w_0, gi_0)
            v0 = space.is_true(w_1)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_2 = space.call_function(space.w_TypeError, gs_map___requires_at_least_one_sequ)
            w_3 = space.type(w_2)
            w_etype, w_evalue = w_3, w_2
            goto = 21

        if goto == 3:
            w_4 = space.len(w_collections)
            w_5 = space.eq(w_4, gi_1)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 4
            else:
                goto = 9

        if goto == 4:
            w_6 = space.is_(w_function, space.w_None)
            v2 = space.is_true(w_6)
            if v2 == True:
                goto = 5
            else:
                goto = 6

        if goto == 5:
            w_7 = space.getitem(w_collections, gi_0)
            w_8 = space.call_function(space.w_list, w_7)
            w_9 = w_8
            goto = 22

        if goto == 6:
            w___1_ = space.newlist([])
            w_10 = space.getitem(w_collections, gi_0)
            w_11 = space.iter(w_10)
            goto = 7

        if goto == 7:
            try:
                w_12 = space.next(w_11)
                goto = 8
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_9 = w___1_
                    goto = 22
                else:raise # unhandled case, should not happen

        if goto == 8:
            w_13 = space.call_function(w_function, w_12)
            w_14 = space.getattr(w___1_, gs_append)
            w_15 = space.call_function(w_14, w_13)
            goto = 7
            continue

        if goto == 9:
            w_iterators = space.newlist([])
            w_16 = space.iter(w_collections)
            goto = 10

        if goto == 10:
            try:
                w_17 = space.next(w_16)
                goto = 11
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 12
                else:raise # unhandled case, should not happen

        if goto == 11:
            w_18 = space.iter(w_17)
            w_19 = space.getattr(w_iterators, gs_append)
            w_20 = space.call_function(w_19, w_18)
            goto = 10
            continue

        if goto == 12:
            w_res = space.newlist([])
            goto = 13

        if goto == 13:
            w_args = space.newlist([])
            w_21 = space.iter(w_iterators)
            w_cont = space.w_False
            goto = 14

        if goto == 14:
            try:
                w_22 = space.next(w_21)
                goto = 15
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 17
                else:raise # unhandled case, should not happen

        if goto == 15:
            w_23 = space.getattr(w_22, gs_next)
            try:
                w_24 = space.call_function(w_23, )
                w_cont_1, w_elem = space.w_True, w_24
                goto = 16
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_cont_1, w_elem = w_cont, space.w_None
                    goto = 16
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 21
                else:raise # unhandled case, should not happen

        if goto == 16:
            w_25 = space.getattr(w_args, gs_append)
            w_26 = space.call_function(w_25, w_elem)
            w_cont = w_cont_1
            goto = 14
            continue

        if goto == 17:
            v3 = space.is_true(w_cont)
            if v3 == True:
                goto = 18
            else:
                w_9 = w_res
                goto = 22

        if goto == 18:
            w_27 = space.is_(w_function, space.w_None)
            v4 = space.is_true(w_27)
            if v4 == True:
                goto = 19
            else:
                goto = 20

        if goto == 19:
            w_28 = space.getattr(w_res, gs_append)
            w_29 = space.call_function(space.w_tuple, w_args)
            w_30 = space.call_function(w_28, w_29)
            goto = 13
            continue

        if goto == 20:
            w_31 = space.getattr(w_res, gs_append)
            _args = gateway.Arguments.fromshape(space, (0, [], True, False), [w_args])
            w_32 = space.call_args(w_function, _args)
            w_33 = space.call_function(w_31, w_32)
            goto = 13
            continue

        if goto == 21:
            raise gOperationError(w_etype, w_evalue)

        if goto == 22:
            return w_9

  fastf_map = map
  fastf_map.__name__ = 'fastf_map'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'filterstring'
## firstlineno 70
##SECTION##
# global declarations
# global object gs_can_t_filter__s_to__s____getitem
# global object gs_join

  def filterstring(space, w_function, w_collection, w_str_type):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.is_(w_function, space.w_None)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_1 = space.type(w_collection)
            w_2 = space.is_(w_1, w_str_type)
            v1 = space.is_true(w_2)
            if v1 == True:
                w_3 = w_collection
                goto = 14
            else:
                goto = 3

        if goto == 3:
            w_res = space.newlist([])
            w_4 = space.len(w_collection)
            w_5 = space.call_function(gtype_xrange, w_4)
            w_6 = space.iter(w_5)
            goto = 4

        if goto == 4:
            try:
                w_7 = space.next(w_6)
                goto = 5
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 12
                else:raise # unhandled case, should not happen

        if goto == 5:
            w_c = space.getitem(w_collection, w_7)
            w_8 = space.is_(w_function, space.w_None)
            v2 = space.is_true(w_8)
            if v2 == True:
                goto = 7
            else:
                goto = 6

        if goto == 6:
            w_9 = space.call_function(w_function, w_c)
            v3 = space.is_true(w_9)
            if v3 == True:
                goto = 7
            else:
                goto = 4
                continue

        if goto == 7:
            w_10 = space.call_function((space.builtin.get(space.str_w(gs_isinstance))), w_c, w_str_type)
            v4 = space.is_true(w_10)
            if v4 == True:
                goto = 11
            else:
                goto = 8

        if goto == 8:
            w_11 = space.getattr(w_str_type, gs___name__)
            w_12 = space.getattr(w_str_type, gs___name__)
            w_13 = space.call_function(space.w_TypeError, gs_can_t_filter__s_to__s____getitem, w_11, w_12)
            w_14 = space.type(w_13)
            w_15 = space.issubtype(w_14, space.w_type)
            v5 = space.is_true(w_15)
            if v5 == True:
                goto = 9
            else:
                goto = 10

        if goto == 9:
            w_16 = space.call_function(w_13, )
            w_17 = space.type(w_16)
            w_etype, w_evalue = w_17, w_16
            goto = 13

        if goto == 10:
            w_18 = space.type(w_13)
            w_etype, w_evalue = w_18, w_13
            goto = 13

        if goto == 11:
            w_19 = space.getattr(w_res, gs_append)
            w_20 = space.call_function(w_19, w_c)
            goto = 4
            continue

        if goto == 12:
            w_21 = space.call_function(w_str_type, )
            w_22 = space.getattr(w_21, gs_join)
            w_23 = space.call_function(w_22, w_res)
            w_3 = w_23
            goto = 14

        if goto == 13:
            raise gOperationError(w_etype, w_evalue)

        if goto == 14:
            return w_3

  fastf_filterstring = filterstring
  fastf_filterstring.__name__ = 'fastf_filterstring'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'filtertuple'
## firstlineno 82
##SECTION##
# global declarations
# global object gtype_xrange
# global object eval_helper

  def filtertuple(space, w_function, w_collection):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.is_(w_function, space.w_None)
            v0 = space.is_true(w_0)
            if v0 == True:
                w_function_1 = space.w_bool
                goto = 2
            else:
                w_function_1 = w_function
                goto = 2

        if goto == 2:
            w_res = space.newlist([])
            w_1 = space.len(w_collection)
            w_2 = space.call_function(gtype_xrange, w_1)
            w_3 = space.iter(w_2)
            goto = 3

        if goto == 3:
            try:
                w_4 = space.next(w_3)
                goto = 4
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 6
                else:raise # unhandled case, should not happen

        if goto == 4:
            w_c = space.getitem(w_collection, w_4)
            w_5 = space.call_function(w_function_1, w_c)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 5
            else:
                goto = 3
                continue

        if goto == 5:
            w_6 = space.getattr(w_res, gs_append)
            w_7 = space.call_function(w_6, w_c)
            goto = 3
            continue

        if goto == 6:
            w_8 = space.call_function(space.w_tuple, w_res)
            goto = 7

        if goto == 7:
            return w_8

  fastf_filtertuple = filtertuple
  fastf_filtertuple.__name__ = 'fastf_filtertuple'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'filter'
## firstlineno 92
##SECTION##
# global declaration
# global object gs_append

  def filter(space, w_function, w_collection):
    """construct a list of those elements of collection for which function
       is True.  If function is None, then return the items in the sequence
       which are True."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.isinstance(w_collection, space.w_str)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_1 = fastf_filterstring(space, w_function, w_collection, space.w_str)
            w_2 = w_1
            goto = 16

        if goto == 3:
            w_3 = space.isinstance(w_collection, space.w_unicode)
            v1 = space.is_true(w_3)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 4:
            w_4 = fastf_filterstring(space, w_function, w_collection, space.w_unicode)
            w_2 = w_4
            goto = 16

        if goto == 5:
            w_5 = space.isinstance(w_collection, space.w_tuple)
            v2 = space.is_true(w_5)
            if v2 == True:
                goto = 6
            else:
                goto = 7

        if goto == 6:
            w_6 = fastf_filtertuple(space, w_function, w_collection)
            w_2 = w_6
            goto = 16

        if goto == 7:
            w_7 = space.is_(w_function, space.w_None)
            v3 = space.is_true(w_7)
            if v3 == True:
                goto = 8
            else:
                goto = 12

        if goto == 8:
            w___1_ = space.newlist([])
            w_8 = space.iter(w_collection)
            goto = 9

        if goto == 9:
            try:
                w_item = space.next(w_8)
                goto = 10
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_2 = w___1_
                    goto = 16
                else:raise # unhandled case, should not happen

        if goto == 10:
            v4 = space.is_true(w_item)
            if v4 == True:
                goto = 11
            else:
                goto = 9
                continue

        if goto == 11:
            w_9 = space.getattr(w___1_, gs_append)
            w_10 = space.call_function(w_9, w_item)
            goto = 9
            continue

        if goto == 12:
            w___2_ = space.newlist([])
            w_11 = space.iter(w_collection)
            goto = 13

        if goto == 13:
            try:
                w_12 = space.next(w_11)
                goto = 14
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_2 = w___2_
                    goto = 16
                else:raise # unhandled case, should not happen

        if goto == 14:
            w_13 = space.call_function(w_function, w_12)
            v5 = space.is_true(w_13)
            if v5 == True:
                goto = 15
            else:
                goto = 13
                continue

        if goto == 15:
            w_14 = space.getattr(w___2_, gs_append)
            w_15 = space.call_function(w_14, w_12)
            goto = 13
            continue

        if goto == 16:
            return w_2

  fastf_filter = filter
  fastf_filter.__name__ = 'fastf_filter'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'zip'
## firstlineno 108
##SECTION##
# global declarations
# global object gs_version_info
# global object g2tuple_1
# global object gi_2
# global object gi_4
# global object gs_zip___requires_at_least_one_sequ

  def zip(space, __args__):
    """return a list of tuples, where the nth tuple contains every
       nth item of each collection.  If the collections have different
       lengths, zip returns a list as long as the shortest collection,
       ignoring the trailing items in the other collections."""

    funcname = "zip"
    signature = [], 'collections', None
    defaults_w = []
    w_collections, = __args__.parse(funcname, signature, defaults_w)
    return fastf_zip(space, w_collections)

  f_zip = zip
  f_zip.__name__ = 'f_zip'

  def zip(space, w_collections):
    """return a list of tuples, where the nth tuple contains every
       nth item of each collection.  If the collections have different
       lengths, zip returns a list as long as the shortest collection,
       ignoring the trailing items in the other collections."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.len(w_collections)
            w_1 = space.eq(w_0, gi_0)
            v0 = space.is_true(w_1)
            if v0 == True:
                goto = 2
            else:
                goto = 6

        if goto == 2:
            w_2 = space.getbuiltinmodule('sys')
            w_3 = space.getattr(w_2, gs_version_info)
            w_4 = space.lt(w_3, g2tuple_1)
            v1 = space.is_true(w_4)
            if v1 == True:
                goto = 3
            else:
                goto = 5

        if goto == 3:
            w_5 = space.call_function(space.w_TypeError, gs_zip___requires_at_least_one_sequ)
            w_6 = space.type(w_5)
            w_7 = space.issubtype(w_6, space.w_type)
            v2 = space.is_true(w_7)
            if v2 == True:
                goto = 4
            else:
                goto = 14

        if goto == 4:
            w_8 = space.call_function(w_5, )
            w_9 = space.type(w_8)
            w_etype, w_evalue = w_9, w_8
            goto = 16

        if goto == 5:
            w_10 = space.newlist([])
            w_11 = w_10
            goto = 17

        if goto == 6:
            w_res = space.newlist([])
            w_iterators = space.newlist([])
            w_12 = space.iter(w_collections)
            goto = 7

        if goto == 7:
            try:
                w_13 = space.next(w_12)
                goto = 8
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 8:
            w_14 = space.iter(w_13)
            w_15 = space.getattr(w_iterators, gs_append)
            w_16 = space.call_function(w_15, w_14)
            goto = 7
            continue

        if goto == 9:
            w_elems = space.newlist([])
            w_17 = space.iter(w_iterators)
            goto = 10

        if goto == 10:
            try:
                w_iterator = space.next(w_17)
                goto = 11
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 13
                else:raise # unhandled case, should not happen

        if goto == 11:
            w_18 = space.getattr(w_elems, gs_append)
            w_19 = space.getattr(w_iterator, gs_next)
            try:
                w_20 = space.call_function(w_19, )
                goto = 12
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_11 = w_res
                    goto = 17
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 16
                else:raise # unhandled case, should not happen

        if goto == 12:
            try:
                w_21 = space.call_function(w_18, w_20)
                goto = 10
                continue
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_11 = w_res
                    goto = 17
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 16
                else:raise # unhandled case, should not happen

        if goto == 13:
            w_22 = space.getattr(w_res, gs_append)
            try:
                w_23 = space.call_function(space.w_tuple, w_elems)
                goto = 15
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_11 = w_res
                    goto = 17
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 16
                else:raise # unhandled case, should not happen

        if goto == 14:
            w_24 = space.type(w_5)
            w_etype, w_evalue = w_24, w_5
            goto = 16

        if goto == 15:
            try:
                w_25 = space.call_function(w_22, w_23)
                goto = 9
                continue
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    w_11 = w_res
                    goto = 17
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 16
                else:raise # unhandled case, should not happen

        if goto == 16:
            raise gOperationError(w_etype, w_evalue)

        if goto == 17:
            return w_11

  fastf_zip = zip
  fastf_zip.__name__ = 'fastf_zip'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'reduce'
## firstlineno 130
##SECTION##
# global declaration
# global object gs_reduce___of_empty_sequence_with_

  def reduce(space, __args__):
    """ Apply function of two arguments cumulatively to the items of
        sequence, from left to right, so as to reduce the sequence to a
        single value.  Optionally begin with an initial value."""

    funcname = "reduce"
    signature = ['function', 'seq'], 'initialt', None
    defaults_w = []
    w_function, w_seq, w_0 = __args__.parse(funcname, signature, defaults_w)
    return fastf_reduce(space, w_function, w_seq, w_0)

  f_reduce = reduce
  f_reduce.__name__ = 'f_reduce'

  def reduce(space, w_function, w_seq, w_0):
    """ Apply function of two arguments cumulatively to the items of
        sequence, from left to right, so as to reduce the sequence to a
        single value.  Optionally begin with an initial value."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_seqiter = space.iter(w_seq)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_1 = space.len(w_0)
            w_2 = space.eq(w_1, gi_1)
            v1 = space.is_true(w_2)
            if v1 == True:
                goto = 6
            else:
                goto = 5

        if goto == 3:
            w_3 = space.getattr(w_seqiter, gs_next)
            try:
                w_4 = space.call_function(w_3, )
                w_5 = w_4
                goto = 7
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 4
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 4:
            w_6 = space.call_function(space.w_TypeError, gs_reduce___of_empty_sequence_with_)
            w_7 = space.type(w_6)
            w_etype, w_evalue = w_7, w_6
            goto = 9

        if goto == 5:
            w_8 = space.call_function(space.w_ValueError, )
            w_9 = space.type(w_8)
            w_etype, w_evalue = w_9, w_8
            goto = 9

        if goto == 6:
            w_10 = space.getitem(w_0, gi_0)
            w_5 = w_10
            goto = 7

        if goto == 7:
            w_11 = space.getattr(w_seqiter, gs_next)
            try:
                w_12 = space.call_function(w_11, )
                goto = 8
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 10
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 9
                else:raise # unhandled case, should not happen

        if goto == 8:
            w_13 = space.call_function(w_function, w_5, w_12)
            w_5 = w_13
            goto = 7
            continue

        if goto == 9:
            raise gOperationError(w_etype, w_evalue)

        if goto == 10:
            return w_5

  fastf_reduce = reduce
  fastf_reduce.__name__ = 'fastf_reduce'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'range'
## firstlineno 164
##SECTION##
# global declarations
# global object gs_isinstance
# global object g2tuple
# global object gs_range___integer_start_argument_e
# global object gs_range___integer_stop_argument_ex
# global object gs_range___integer_step_argument_ex
# global object gs_range___arg_3_must_not_be_zero

  def range(space, __args__):
    """ returns a list of integers in arithmetic position from start (defaults
        to zero) to stop - 1 by step (defaults to 1).  Use a negative step to
        get a list in decending order."""

    funcname = "range"
    signature = ['x', 'y', 'step'], None, None
    defaults_w = [space.w_None, gi_1]
    w_x, w_y, w_step = __args__.parse(funcname, signature, defaults_w)
    return fastf_range(space, w_x, w_y, w_step)

  f_range = range
  f_range.__name__ = 'f_range'

  def range(space, w_x, w_y, w_step):
    """ returns a list of integers in arithmetic position from start (defaults
        to zero) to stop - 1 by step (defaults to 1).  Use a negative step to
        get a list in decending order."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.is_(w_y, space.w_None)
            v0 = space.is_true(w_0)
            if v0 == True:
                w_start, w_stop = gi_0, w_x
                goto = 2
            else:
                w_start, w_stop = w_x, w_y
                goto = 2

        if goto == 2:
            w_1 = space.call_function((space.builtin.get(space.str_w(gs_isinstance))), w_start, g2tuple)
            v1 = space.is_true(w_1)
            if v1 == True:
                goto = 5
            else:
                goto = 3

        if goto == 3:
            w_2 = space.type(w_start)
            w_3 = space.mod(gs_range___integer_start_argument_e, w_2)
            w_4 = space.call_function(space.w_TypeError, w_3)
            w_5 = space.type(w_4)
            w_6 = space.issubtype(w_5, space.w_type)
            v2 = space.is_true(w_6)
            if v2 == True:
                goto = 4
            else:
                goto = 9

        if goto == 4:
            w_7 = space.call_function(w_4, )
            w_8 = space.type(w_7)
            w_etype, w_evalue = w_8, w_7
            goto = 26

        if goto == 5:
            w_9 = space.call_function((space.builtin.get(space.str_w(gs_isinstance))), w_stop, g2tuple)
            v3 = space.is_true(w_9)
            if v3 == True:
                goto = 8
            else:
                goto = 6

        if goto == 6:
            w_10 = space.type(w_stop)
            w_11 = space.mod(gs_range___integer_stop_argument_ex, w_10)
            w_12 = space.call_function(space.w_TypeError, w_11)
            w_13 = space.type(w_12)
            w_14 = space.issubtype(w_13, space.w_type)
            v4 = space.is_true(w_14)
            if v4 == True:
                goto = 7
            else:
                goto = 14

        if goto == 7:
            w_15 = space.call_function(w_12, )
            w_16 = space.type(w_15)
            w_etype, w_evalue = w_16, w_15
            goto = 26

        if goto == 8:
            w_17 = space.call_function((space.builtin.get(space.str_w(gs_isinstance))), w_step, g2tuple)
            v5 = space.is_true(w_17)
            if v5 == True:
                goto = 12
            else:
                goto = 10

        if goto == 9:
            w_18 = space.type(w_4)
            w_etype, w_evalue = w_18, w_4
            goto = 26

        if goto == 10:
            w_19 = space.type(w_step)
            w_20 = space.mod(gs_range___integer_step_argument_ex, w_19)
            w_21 = space.call_function(space.w_TypeError, w_20)
            w_22 = space.type(w_21)
            w_23 = space.issubtype(w_22, space.w_type)
            v6 = space.is_true(w_23)
            if v6 == True:
                goto = 11
            else:
                goto = 17

        if goto == 11:
            w_24 = space.call_function(w_21, )
            w_25 = space.type(w_24)
            w_etype, w_evalue = w_25, w_24
            goto = 26

        if goto == 12:
            w_26 = space.eq(w_step, gi_0)
            v7 = space.is_true(w_26)
            if v7 == True:
                goto = 13
            else:
                goto = 15

        if goto == 13:
            w_27 = space.call_function(space.w_ValueError, gs_range___arg_3_must_not_be_zero)
            w_28 = space.type(w_27)
            w_etype, w_evalue = w_28, w_27
            goto = 26

        if goto == 14:
            w_29 = space.type(w_12)
            w_etype, w_evalue = w_29, w_12
            goto = 26

        if goto == 15:
            w_30 = space.gt(w_step, gi_0)
            v8 = space.is_true(w_30)
            if v8 == True:
                goto = 16
            else:
                goto = 20

        if goto == 16:
            w_31 = space.le(w_stop, w_start)
            v9 = space.is_true(w_31)
            if v9 == True:
                goto = 18
            else:
                goto = 19

        if goto == 17:
            w_32 = space.type(w_21)
            w_etype, w_evalue = w_32, w_21
            goto = 26

        if goto == 18:
            w_33 = space.newlist([])
            w_34 = w_33
            goto = 27

        if goto == 19:
            w_35 = space.sub(w_stop, w_start)
            w_36 = space.add(w_35, w_step)
            w_37 = space.sub(w_36, gi_1)
            w_38 = space.div(w_37, w_step)
            w_howmany = w_38
            goto = 23

        if goto == 20:
            w_39 = space.ge(w_stop, w_start)
            v10 = space.is_true(w_39)
            if v10 == True:
                goto = 21
            else:
                goto = 22

        if goto == 21:
            w_40 = space.newlist([])
            w_34 = w_40
            goto = 27

        if goto == 22:
            w_41 = space.sub(w_start, w_stop)
            w_42 = space.sub(w_41, w_step)
            w_43 = space.sub(w_42, gi_1)
            w_44 = space.neg(w_step)
            w_45 = space.div(w_43, w_44)
            w_howmany = w_45
            goto = 23

        if goto == 23:
            w_46 = space.newlist([space.w_None])
            w_arr = space.mul(w_46, w_howmany)
            w_i, w_n = w_start, gi_0
            goto = 24

        if goto == 24:
            w_47 = space.lt(w_n, w_howmany)
            v11 = space.is_true(w_47)
            if v11 == True:
                goto = 25
            else:
                w_34 = w_arr
                goto = 27

        if goto == 25:
            w_48 = space.setitem(w_arr, w_n, w_i)
            w_49 = space.inplace_add(w_i, w_step)
            w_50 = space.inplace_add(w_n, gi_1)
            w_i, w_n = w_49, w_50
            goto = 24
            continue

        if goto == 26:
            raise gOperationError(w_etype, w_evalue)

        if goto == 27:
            return w_34

  fastf_range = range
  fastf_range.__name__ = 'fastf_range'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    '_identity'
## firstlineno 211
##SECTION##
  def _identity(space, w_0):
    goto = 2 # startblock
    while True:

        if goto == 1:
            return w_0

        if goto == 2:
            goto = 1
            continue

  fastf__identity = _identity
  fastf__identity.__name__ = 'fastf__identity'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'min'
## firstlineno 215
##SECTION##
# global declarations
# global object g0dict_2
# global object g1tuple_1
# global object gs_gt
# global object gs_cannot_import_name__gt_

  def min(space, __args__):
    """return the smallest number in a list,
    or its smallest argument if more than one is given."""

    funcname = "min"
    signature = [], 'arr', 'kwargs'
    defaults_w = []
    w_2, w_3 = __args__.parse(funcname, signature, defaults_w)
    return fastf_min(space, w_2, w_3)

  f_min = min
  f_min.__name__ = 'f_min'

  def min(space, w_2, w_3):
    """return the smallest number in a list,
    or its smallest argument if more than one is given."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs_operator, g0dict_2, space.w_None, g1tuple_1)
            try:
                w_1 = space.getattr(w_0, gs_gt)
                goto = 2
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    (w_etype, w_evalue) = (space.w_ImportError,
                     gs_cannot_import_name__gt_)
                    goto = 3
                else:raise # unhandled case, should not happen

        if goto == 2:
            _args = gateway.Arguments.fromshape(space, (2, [], True, True), [w_1, gs_min, w_2, w_3])
            w_4 = space.call_args(gfunc_min_max, _args)
            goto = 4

        if goto == 3:
            raise gOperationError(w_etype, w_evalue)

        if goto == 4:
            return w_4

  fastf_min = min
  fastf_min.__name__ = 'fastf_min'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'min_max'
## firstlineno 222
##SECTION##
# global declarations
# global object gs_pop
# global object gs_key
# global object gs__s___got_an_unexpected_keyword_a
# global object gs__s___takes_at_least_one_argument
# global object gs__s___arg_is_an_empty_sequence

  def min_max(space, __args__):
    funcname = "min_max"
    signature = ['comp', 'funcname'], 'arr', 'kwargs'
    defaults_w = []
    w_comp, w_2, w_arr, w_kwargs = __args__.parse(funcname, signature, defaults_w)
    return fastf_min_max(space, w_comp, w_2, w_arr, w_kwargs)

  f_min_max = min_max
  f_min_max.__name__ = 'f_min_max'

  def min_max(space, w_comp, w_2, w_arr, w_kwargs):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_kwargs, gs_pop)
            w_key = space.call_function(w_0, gs_key, gfunc__identity)
            w_1 = space.len(w_kwargs)
            v0 = space.is_true(w_1)
            if v0 == True:
                goto = 2
            else:
                goto = 6

        if goto == 2:
            w_3 = space.mod(gs__s___got_an_unexpected_keyword_a, w_2)
            w_4 = space.is_(w_3, space.w_None)
            v1 = space.is_true(w_4)
            if v1 == True:
                goto = 9
            else:
                goto = 10

        if goto == 3:
            w_5 = space.call_function(space.w_TypeError, )
            w_6 = space.type(w_5)
            w_etype, w_evalue = w_6, w_5
            goto = 21

        if goto == 4:
            w_7 = space.call_function(space.w_TypeError, w_8)
            w_9 = space.type(w_7)
            w_etype, w_evalue = w_9, w_7
            goto = 21

        if goto == 5:
            w_10 = space.type(w_8)
            w_11 = space.issubtype(w_10, space.w_TypeError)
            v2 = space.is_true(w_11)
            if v2 == True:
                w_etype, w_evalue = w_10, w_8
                goto = 21
            else:
                goto = 4
                continue

        if goto == 6:
            v3 = space.is_true(w_arr)
            if v3 == True:
                goto = 8
            else:
                goto = 7

        if goto == 7:
            w_8 = space.mod(gs__s___takes_at_least_one_argument, w_2)
            w_12 = space.is_(w_8, space.w_None)
            v4 = space.is_true(w_12)
            if v4 == True:
                goto = 3
                continue
            else:
                goto = 5
                continue

        if goto == 8:
            w_13 = space.len(w_arr)
            w_14 = space.eq(w_13, gi_1)
            v5 = space.is_true(w_14)
            if v5 == True:
                goto = 12
            else:
                w_15 = w_arr
                goto = 13

        if goto == 9:
            w_16 = space.call_function(space.w_TypeError, )
            w_17 = space.type(w_16)
            w_etype, w_evalue = w_17, w_16
            goto = 21

        if goto == 10:
            w_18 = space.type(w_3)
            w_19 = space.issubtype(w_18, space.w_TypeError)
            v6 = space.is_true(w_19)
            if v6 == True:
                w_etype, w_evalue = w_18, w_3
                goto = 21
            else:
                goto = 11

        if goto == 11:
            w_20 = space.call_function(space.w_TypeError, w_3)
            w_21 = space.type(w_20)
            w_etype, w_evalue = w_21, w_20
            goto = 21

        if goto == 12:
            w_22 = space.getitem(w_arr, gi_0)
            w_15 = w_22
            goto = 13

        if goto == 13:
            w_iterator = space.iter(w_15)
            w_23 = space.getattr(w_iterator, gs_next)
            try:
                w_min_max_val = space.call_function(w_23, )
                goto = 15
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 14
                elif e.match(space, space.w_Exception):
                    w_etype, w_evalue = e.w_type, e.w_value
                    goto = 21
                else:raise # unhandled case, should not happen

        if goto == 14:
            w_24 = space.mod(gs__s___arg_is_an_empty_sequence, w_2)
            w_25 = space.is_(w_24, space.w_None)
            v7 = space.is_true(w_25)
            if v7 == True:
                goto = 18
            else:
                goto = 19

        if goto == 15:
            w_26 = space.call_function(w_key, w_min_max_val)
            w_27 = space.iter(w_iterator)
            w_min_max_val_1, w_keyed_min_max_val = w_min_max_val, w_26
            goto = 16

        if goto == 16:
            try:
                w_i = space.next(w_27)
                goto = 17
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_StopIteration):
                    goto = 22
                else:raise # unhandled case, should not happen

        if goto == 17:
            w_28 = space.call_function(w_key, w_i)
            w_29 = space.call_function(w_comp, w_keyed_min_max_val, w_28)
            v8 = space.is_true(w_29)
            if v8 == True:
                w_min_max_val_1, w_keyed_min_max_val = w_i, w_28
                goto = 16
                continue
            else:
                goto = 16
                continue

        if goto == 18:
            w_30 = space.call_function(space.w_ValueError, )
            w_31 = space.type(w_30)
            w_etype, w_evalue = w_31, w_30
            goto = 21

        if goto == 19:
            w_32 = space.type(w_24)
            w_33 = space.issubtype(w_32, space.w_ValueError)
            v9 = space.is_true(w_33)
            if v9 == True:
                w_etype, w_evalue = w_32, w_24
                goto = 21
            else:
                goto = 20

        if goto == 20:
            w_34 = space.call_function(space.w_ValueError, w_24)
            w_35 = space.type(w_34)
            w_etype, w_evalue = w_35, w_34
            goto = 21

        if goto == 21:
            raise gOperationError(w_etype, w_evalue)

        if goto == 22:
            return w_min_max_val_1

  fastf_min_max = min_max
  fastf_min_max.__name__ = 'fastf_min_max'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'max'
## firstlineno 248
##SECTION##
# global declarations
# global object gs_operator
# global object g0dict_1
# global object g1tuple
# global object gs_lt
# global object gs_cannot_import_name__lt_

  def max(space, __args__):
    """return the largest number in a list,
    or its largest argument if more than one is given."""

    funcname = "max"
    signature = [], 'arr', 'kwargs'
    defaults_w = []
    w_2, w_3 = __args__.parse(funcname, signature, defaults_w)
    return fastf_max(space, w_2, w_3)

  f_max = max
  f_max.__name__ = 'f_max'

  def max(space, w_2, w_3):
    """return the largest number in a list,
    or its largest argument if more than one is given."""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs_operator, g0dict_1, space.w_None, g1tuple)
            try:
                w_1 = space.getattr(w_0, gs_lt)
                goto = 2
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    (w_etype, w_evalue) = (space.w_ImportError,
                     gs_cannot_import_name__lt_)
                    goto = 3
                else:raise # unhandled case, should not happen

        if goto == 2:
            _args = gateway.Arguments.fromshape(space, (2, [], True, True), [w_1, gs_max, w_2, w_3])
            w_4 = space.call_args(gfunc_min_max, _args)
            goto = 4

        if goto == 3:
            raise gOperationError(w_etype, w_evalue)

        if goto == 4:
            return w_4

  fastf_max = max
  fastf_max.__name__ = 'fastf_max'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    '__init__'
## firstlineno 263
##SECTION##
# global declaration
# global object gi_0

  def __init__(space, w_self, w_collection):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.iter(w_collection)
            w_1 = space.setattr(w_self, gs__iter, w_0)
            w_2 = space.setattr(w_self, gs__index, gi_0)
            w_3 = space.w_None
            goto = 2

        if goto == 2:
            return w_3

  fastf_enumerate___init__ = __init__
  fastf_enumerate___init__.__name__ = 'fastf_enumerate___init__'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'next'
## firstlineno 267
##SECTION##
# global declarations
# global object gs__iter
# global object gs__s_object_has_no_next___method
# global object gs__index
# global object gi_1

  def next(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            try:
                w_0 = space.getattr(w_self, gs__iter)
                goto = 2
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 3
                else:raise # unhandled case, should not happen

        if goto == 2:
            try:
                w_next = space.getattr(w_0, gs_next)
                goto = 6
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 3
                else:raise # unhandled case, should not happen

        if goto == 3:
            w_1 = space.getattr(w_self, gs__iter)
            w_2 = space.type(w_1)
            w_3 = space.getattr(w_2, gs___name__)
            w_4 = space.newtuple([w_3])
            w_5 = space.mod(gs__s_object_has_no_next___method, w_4)
            w_6 = space.call_function(space.w_TypeError, w_5)
            w_7 = space.type(w_6)
            w_8 = space.issubtype(w_7, space.w_type)
            v0 = space.is_true(w_8)
            if v0 == True:
                goto = 5
            else:
                goto = 4

        if goto == 4:
            w_9 = space.type(w_6)
            w_etype, w_evalue = w_9, w_6
            goto = 7

        if goto == 5:
            w_10 = space.call_function(w_6, )
            w_11 = space.type(w_10)
            w_etype, w_evalue = w_11, w_10
            goto = 7

        if goto == 6:
            w_12 = space.getattr(w_self, gs__index)
            w_13 = space.call_function(w_next, )
            w_14 = space.newtuple([w_12, w_13])
            w_15 = space.getattr(w_self, gs__index)
            w_16 = space.inplace_add(w_15, gi_1)
            w_17 = space.setattr(w_self, gs__index, w_16)
            goto = 8

        if goto == 7:
            raise gOperationError(w_etype, w_evalue)

        if goto == 8:
            return w_14

  fastf_enumerate_next = next
  fastf_enumerate_next.__name__ = 'fastf_enumerate_next'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    '__iter__'
## firstlineno 278
##SECTION##
  def __iter__(space, w_0):
    goto = 2 # startblock
    while True:

        if goto == 1:
            return w_0

        if goto == 2:
            goto = 1
            continue

  fastf_enumerate___iter__ = __iter__
  fastf_enumerate___iter__.__name__ = 'fastf_enumerate___iter__'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'sorted'
## firstlineno 284
##SECTION##
# global declaration
# global object gs_sort

  def sorted(space, __args__):
    """sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list"""

    funcname = "sorted"
    signature = ['lst', 'cmp', 'key', 'reverse'], None, None
    defaults_w = [space.w_None, space.w_None, space.w_None]
    w_lst, w_cmp, w_key, w_reverse = __args__.parse(funcname, signature, defaults_w)
    return fastf_sorted(space, w_lst, w_cmp, w_key, w_reverse)

  f_sorted = sorted
  f_sorted.__name__ = 'f_sorted'

  def sorted(space, w_lst, w_cmp, w_key, w_reverse):
    """sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list"""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function(space.w_list, w_lst)
            w_1 = space.getattr(w_0, gs_sort)
            w_2 = space.call_function(w_1, w_cmp, w_key, w_reverse)
            goto = 2

        if goto == 2:
            return w_0

  fastf_sorted = sorted
  fastf_sorted.__name__ = 'fastf_sorted'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'reversed'
## firstlineno 290
##SECTION##
# global declarations
# global object gs_hasattr
# global object gs___reversed__
# global object gs___getitem__
# global object gs_argument_to_reversed___must_be_a

  def reversed(space, w_1):
    """reversed(sequence) -> reverse iterator over values of the sequence"""
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function((space.builtin.get(space.str_w(gs_hasattr))), w_1, gs___reversed__)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_2 = space.getattr(w_1, gs___reversed__)
            w_3 = space.call_function(w_2, )
            w_4 = w_3
            goto = 9

        if goto == 3:
            w_5 = space.call_function((space.builtin.get(space.str_w(gs_hasattr))), w_1, gs___getitem__)
            v1 = space.is_true(w_5)
            if v1 == True:
                goto = 7
            else:
                goto = 4

        if goto == 4:
            w_6 = space.call_function(space.w_TypeError, gs_argument_to_reversed___must_be_a)
            w_7 = space.type(w_6)
            w_8 = space.issubtype(w_7, space.w_type)
            v2 = space.is_true(w_8)
            if v2 == True:
                goto = 6
            else:
                goto = 5

        if goto == 5:
            w_9 = space.type(w_6)
            w_etype, w_evalue = w_9, w_6
            goto = 8

        if goto == 6:
            w_10 = space.call_function(w_6, )
            w_11 = space.type(w_10)
            w_etype, w_evalue = w_11, w_10
            goto = 8

        if goto == 7:
            w_12 = space.call_function(gcls_reversed_iterator, w_1)
            w_4 = w_12
            goto = 9

        if goto == 8:
            raise gOperationError(w_etype, w_evalue)

        if goto == 9:
            return w_4

  fastf_reversed = reversed
  fastf_reversed.__name__ = 'fastf_reversed'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    '__init__'
## firstlineno 301
##SECTION##
  def __init__(space, w_self, w_seq):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.setattr(w_self, gs_seq, w_seq)
            w_1 = space.len(w_seq)
            w_2 = space.setattr(w_self, gs_remaining, w_1)
            w_3 = space.w_None
            goto = 2

        if goto == 2:
            return w_3

  fastf_reversed_iterator___init__ = __init__
  fastf_reversed_iterator___init__.__name__ = 'fastf_reversed_iterator___init__'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    '__iter__'
## firstlineno 305
##SECTION##
  def __iter__(space, w_0):
    goto = 2 # startblock
    while True:

        if goto == 1:
            return w_0

        if goto == 2:
            goto = 1
            continue

  fastf_reversed_iterator___iter__ = __iter__
  fastf_reversed_iterator___iter__.__name__ = 'fastf_reversed_iterator___iter__'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'next'
## firstlineno 308
##SECTION##
  def next(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_remaining)
            w_1 = space.getattr(w_self, gs_seq)
            w_2 = space.len(w_1)
            w_3 = space.gt(w_0, w_2)
            v0 = space.is_true(w_3)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_4 = space.setattr(w_self, gs_remaining, gi_0)
            goto = 3

        if goto == 3:
            w_5 = space.getattr(w_self, gs_remaining)
            w_6 = space.gt(w_5, gi_0)
            v1 = space.is_true(w_6)
            if v1 == True:
                goto = 4
            else:
                goto = 5

        if goto == 4:
            w_7 = space.inplace_sub(w_5, gi_1)
            w_8 = space.getattr(w_self, gs_seq)
            w_9 = space.getitem(w_8, w_7)
            w_10 = space.setattr(w_self, gs_remaining, w_7)
            goto = 7

        if goto == 5:
            w_evalue = space.call_function(space.w_StopIteration, )
            w_etype = space.type(w_evalue)
            goto = 6

        if goto == 6:
            raise gOperationError(w_etype, w_evalue)

        if goto == 7:
            return w_9

  fastf_reversed_iterator_next = next
  fastf_reversed_iterator_next.__name__ = 'fastf_reversed_iterator_next'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    '__reduce__'
## firstlineno 325
##SECTION##
  def __reduce__(space, w_self):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_self, gs_seq)
            w_1 = space.getattr(w_self, gs_remaining)
            w_2 = space.newtuple([w_0, w_1])
            w_3 = space.newtuple([gfunc_make_reversed_iterator, w_2])
            goto = 2

        if goto == 2:
            return w_3

  fastf_reversed_iterator___reduce__ = __reduce__
  fastf_reversed_iterator___reduce__.__name__ = 'fastf_reversed_iterator___reduce__'

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    'make_reversed_iterator'
## firstlineno 329
##SECTION##
# global declarations
# global object g23dict
# global object gs_filterstring
# global object gfunc_filterstring
# global object gs_enumerate
# global object gcls_enumerate
# global object gs___module__
# global object gs___builtin__
# global object gs___doc__
# global object gs_reduce
# global object gfunc_reduce
# global object gs_filtertuple
# global object gfunc_filtertuple
# global object gs_apply
# global object gfunc_apply
# global object gs_zip
# global object gfunc_zip
# global object gs_min
# global object gfunc_min
# global object gs_sum
# global object gfunc_sum
# global object gs_range
# global object gfunc_range
# global object gs_min_max
# global object gfunc_min_max
# global object gs__identity
# global object gfunc__identity
# global object gs_reversed_iterator
# global object gcls_reversed_iterator
# global object gs_reversed
# global object gfunc_reversed
# global object gs_map
# global object gfunc_map
# global object gs_max
# global object gfunc_max
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_sorted
# global object gfunc_sorted
# global object gs__install_pickle_support_for_reve
# global object gfunc__install_pickle_support_for_reversed_iterato
# global object gs___name__
# global object gs_filter
# global object gfunc_filter
# global object gs_make_reversed_iterator
# global object gfunc_make_reversed_iterator
# global object gbltinmethod___new__
# global object gs___new__
# global object gs_seq
# global object gs_remaining

  def make_reversed_iterator(space, w_seq, w_remaining):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function(gbltinmethod___new__, gcls_reversed_iterator)
            w_1 = space.setattr(w_0, gs_seq, w_seq)
            w_2 = space.setattr(w_0, gs_remaining, w_remaining)
            goto = 2

        if goto == 2:
            return w_0

  fastf_make_reversed_iterator = make_reversed_iterator
  fastf_make_reversed_iterator.__name__ = 'fastf_make_reversed_iterator'

# global declarations
# global object gs___init__
# global object gfunc_reversed_iterator___init__
# global object gs___iter__
# global object gfunc_reversed_iterator___iter__
# global object gs___reduce__
# global object gfunc_reversed_iterator___reduce__
# global object gs_next
# global object gfunc_reversed_iterator_next
# global object gfunc_enumerate___init__
# global object gfunc_enumerate___iter__
# global object gfunc_enumerate_next

##SECTION##
## filename    'module/__builtin__/app_functional.py'
## function    '_install_pickle_support_for_reversed_iterator'
## firstlineno 336
##SECTION##
# global declarations
# global object gs___import__
# global object gs__pickle_support
# global object g0dict

  def _install_pickle_support_for_reversed_iterator(space):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs__pickle_support, g0dict, space.w_None, space.w_None)
            w_1 = space.setattr(gfunc_make_reversed_iterator, gs___module__, gs__pickle_support)
            w_2 = space.setattr(w_0, gs_make_reversed_iterator, gfunc_make_reversed_iterator)
            w_3 = space.w_None
            goto = 2

        if goto == 2:
            return w_3

  fastf__install_pickle_support_for_reversed_iterato = _install_pickle_support_for_reversed_iterator
  fastf__install_pickle_support_for_reversed_iterato.__name__ = 'fastf__install_pickle_support_for_reversed_iterato'

##SECTION##
  w__doc__ = space.new_interned_str(__doc__)
  g23dict = space.newdict()
  gs_filterstring = space.new_interned_str('filterstring')
  from pypy.interpreter import gateway
  gfunc_filterstring = space.wrap(gateway.interp2app(fastf_filterstring, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root, gateway.W_Root]))
  space.setitem(g23dict, gs_filterstring, gfunc_filterstring)
  gs_enumerate = space.new_interned_str('enumerate')
  gs___module__ = space.new_interned_str('__module__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  gs___doc__ = space.new_interned_str('__doc__')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs___builtin__)
  _doc = space.wrap("""enumerate(iterable) -> iterator for (index, value) of iterable.

Return an enumerate object.  iterable must be an other object that supports
iteration.  The enumerate object yields pairs containing a count (from
zero) and a value yielded by the iterable argument.  enumerate is useful
for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...""")
  space.setitem(_dic, gs___doc__, _doc)
  _bases = space.newtuple([space.w_object])
  _args = space.newtuple([gs_enumerate, _bases, _dic])
  gcls_enumerate = space.call(space.w_type, _args)
  space.setitem(g23dict, gs_enumerate, gcls_enumerate)
  gs_reduce = space.new_interned_str('reduce')
  gfunc_reduce = space.wrap(gateway.interp2app(f_reduce, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_reduce, gfunc_reduce)
  gs_filtertuple = space.new_interned_str('filtertuple')
  gfunc_filtertuple = space.wrap(gateway.interp2app(fastf_filtertuple, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g23dict, gs_filtertuple, gfunc_filtertuple)
  gs_apply = space.new_interned_str('apply')
  gfunc_apply = space.wrap(gateway.interp2app(f_apply, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_apply, gfunc_apply)
  gs_zip = space.new_interned_str('zip')
  gfunc_zip = space.wrap(gateway.interp2app(f_zip, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_zip, gfunc_zip)
  gs_min = space.new_interned_str('min')
  gfunc_min = space.wrap(gateway.interp2app(f_min, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_min, gfunc_min)
  gs_sum = space.new_interned_str('sum')
  gfunc_sum = space.wrap(gateway.interp2app(f_sum, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_sum, gfunc_sum)
  gs_range = space.new_interned_str('range')
  gfunc_range = space.wrap(gateway.interp2app(f_range, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_range, gfunc_range)
  gs_min_max = space.new_interned_str('min_max')
  gfunc_min_max = space.wrap(gateway.interp2app(f_min_max, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_min_max, gfunc_min_max)
  gs__identity = space.new_interned_str('_identity')
  gfunc__identity = space.wrap(gateway.interp2app(fastf__identity, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g23dict, gs__identity, gfunc__identity)
  gs_reversed_iterator = space.new_interned_str('reversed_iterator')
  _dic = space.newdict()
  space.setitem(_dic, gs___module__, gs___builtin__)
  _bases = space.newtuple([space.w_object])
  _args = space.newtuple([gs_reversed_iterator, _bases, _dic])
  gcls_reversed_iterator = space.call(space.w_type, _args)
  space.setitem(g23dict, gs_reversed_iterator, gcls_reversed_iterator)
  gs_reversed = space.new_interned_str('reversed')
  gfunc_reversed = space.wrap(gateway.interp2app(fastf_reversed, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g23dict, gs_reversed, gfunc_reversed)
  gs_map = space.new_interned_str('map')
  gfunc_map = space.wrap(gateway.interp2app(f_map, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_map, gfunc_map)
  gs_max = space.new_interned_str('max')
  gfunc_max = space.wrap(gateway.interp2app(f_max, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_max, gfunc_max)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/module/__builtin__/app_functional.py""")
  space.setitem(g23dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_sorted = space.new_interned_str('sorted')
  gfunc_sorted = space.wrap(gateway.interp2app(f_sorted, unwrap_spec=[gateway.ObjSpace, gateway.Arguments]))
  space.setitem(g23dict, gs_sorted, gfunc_sorted)
  gs__install_pickle_support_for_reve = space.new_interned_str(
"""_install_pickle_support_for_reversed_iterator""")
  gfunc__install_pickle_support_for_reversed_iterato = space.wrap(gateway.interp2app(fastf__install_pickle_support_for_reversed_iterato, unwrap_spec=[gateway.ObjSpace, ]))
  space.setitem(g23dict, gs__install_pickle_support_for_reve, gfunc__install_pickle_support_for_reversed_iterato)
  gs___name__ = space.new_interned_str('__name__')
  space.setitem(g23dict, gs___name__, gs___builtin__)
  space.setitem(g23dict, gs___doc__, w__doc__)
  gs_filter = space.new_interned_str('filter')
  gfunc_filter = space.wrap(gateway.interp2app(fastf_filter, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g23dict, gs_filter, gfunc_filter)
  gs_make_reversed_iterator = space.new_interned_str('make_reversed_iterator')
  gfunc_make_reversed_iterator = space.wrap(gateway.interp2app(fastf_make_reversed_iterator, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g23dict, gs_make_reversed_iterator, gfunc_make_reversed_iterator)
  gs___new__ = space.new_interned_str('__new__')
  gbltinmethod___new__ = space.getattr(space.w_object, gs___new__)
  gs_seq = space.new_interned_str('seq')
  gs_remaining = space.new_interned_str('remaining')
  gs___init__ = space.new_interned_str('__init__')
  gfunc_reversed_iterator___init__ = space.wrap(gateway.interp2app(fastf_reversed_iterator___init__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setattr(gcls_reversed_iterator, gs___init__, gfunc_reversed_iterator___init__)
  gs___iter__ = space.new_interned_str('__iter__')
  gfunc_reversed_iterator___iter__ = space.wrap(gateway.interp2app(fastf_reversed_iterator___iter__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_reversed_iterator, gs___iter__, gfunc_reversed_iterator___iter__)
  gs___reduce__ = space.new_interned_str('__reduce__')
  gfunc_reversed_iterator___reduce__ = space.wrap(gateway.interp2app(fastf_reversed_iterator___reduce__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_reversed_iterator, gs___reduce__, gfunc_reversed_iterator___reduce__)
  gs_next = space.new_interned_str('next')
  gfunc_reversed_iterator_next = space.wrap(gateway.interp2app(fastf_reversed_iterator_next, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_reversed_iterator, gs_next, gfunc_reversed_iterator_next)
  gfunc_enumerate___init__ = space.wrap(gateway.interp2app(fastf_enumerate___init__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setattr(gcls_enumerate, gs___init__, gfunc_enumerate___init__)
  gfunc_enumerate___iter__ = space.wrap(gateway.interp2app(fastf_enumerate___iter__, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_enumerate, gs___iter__, gfunc_enumerate___iter__)
  gfunc_enumerate_next = space.wrap(gateway.interp2app(fastf_enumerate_next, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setattr(gcls_enumerate, gs_next, gfunc_enumerate_next)
  gs__iter = space.new_interned_str('_iter')
  from pypy.interpreter.error import OperationError as gOperationError
  gs__s_object_has_no_next___method = space.new_interned_str(
"""%s object has no next() method""")
  gs__index = space.new_interned_str('_index')
  gi_1 = space.wrap(1)
  gi_0 = space.wrap(0)
  gs_append = space.new_interned_str('append')
  gs___import__ = space.new_interned_str('__import__')
  gs__pickle_support = space.new_interned_str('_pickle_support')
  g0dict = space.newdict()
  gs_sort = space.new_interned_str('sort')
  gs_operator = space.new_interned_str('operator')
  g0dict_1 = space.newdict()
  gs_lt = space.new_interned_str('lt')
  g1tuple = space.newtuple([gs_lt])
  gs_cannot_import_name__lt_ = space.new_interned_str("cannot import name 'lt'")
  gs_map___requires_at_least_one_sequ = space.new_interned_str(
"""map() requires at least one sequence""")
  gs_hasattr = space.new_interned_str('hasattr')
  gs___reversed__ = space.new_interned_str('__reversed__')
  gs___getitem__ = space.new_interned_str('__getitem__')
  gs_argument_to_reversed___must_be_a = space.new_interned_str(
"""argument to reversed() must be a sequence""")
  gs_pop = space.new_interned_str('pop')
  gs_key = space.new_interned_str('key')
  gs__s___got_an_unexpected_keyword_a = space.new_interned_str(
"""%s() got an unexpected keyword argument""")
  gs__s___takes_at_least_one_argument = space.new_interned_str(
"""%s() takes at least one argument""")
  gs__s___arg_is_an_empty_sequence = space.new_interned_str('%s() arg is an empty sequence')
  gs_isinstance = space.new_interned_str('isinstance')
  g2tuple = space.newtuple([space.w_int, space.w_long])
  gs_range___integer_start_argument_e = space.new_interned_str(
"""range() integer start argument expected, got %s""")
  gs_range___integer_stop_argument_ex = space.new_interned_str(
"""range() integer stop argument expected, got %s""")
  gs_range___integer_step_argument_ex = space.new_interned_str(
"""range() integer step argument expected, got %s""")
  gs_range___arg_3_must_not_be_zero = space.new_interned_str(
"""range() arg 3 must not be zero""")
  g0dict_2 = space.newdict()
  gs_gt = space.new_interned_str('gt')
  g1tuple_1 = space.newtuple([gs_gt])
  gs_cannot_import_name__gt_ = space.new_interned_str("cannot import name 'gt'")
  gs_version_info = space.new_interned_str('version_info')
  gi_2 = space.wrap(2)
  gi_4 = space.wrap(4)
  g2tuple_1 = space.newtuple([gi_2, gi_4])
  gs_zip___requires_at_least_one_sequ = space.new_interned_str(
"""zip() requires at least one sequence""")
  g0tuple = space.newtuple([])
  g0dict_3 = space.newdict()
  def eval_helper(expr):
      dic = space.newdict()
      if "types." in expr:
          space.exec_("import types", dic, dic, hidden_applevel=True)
      else:
          space.exec_("", dic, dic, hidden_applevel=True)
      return space.eval(expr, dic, dic, hidden_applevel=True)
  gtype_xrange = eval_helper('xrange')
  gs_reduce___of_empty_sequence_with_ = space.new_interned_str(
"""reduce() of empty sequence with no initial value""")
  gs_can_t_filter__s_to__s____getitem = space.new_interned_str(
"""can't filter %s to %s: __getitem__ returned different type""")
  gs_join = space.new_interned_str('join')
  return g23dict


from pypy._cache import known_code
known_code['bfd6e4221cb21d34fb669d4e2504172c'] = init__builtin__
