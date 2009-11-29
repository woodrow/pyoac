# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'pyopcode_77fe4d1b6e496ab15705292ceb905ea8')
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
## function    'sys_stdout'
## firstlineno 1250
##SECTION##
# global declarations
# global object gs_stdout
# global object gs_lost_sys_stdout

  def sys_stdout(space):
    goto = 1 # startblock
    while True:

        if goto == 1:
            try:
                w_0 = space.getattr(mod_sys, gs_stdout)
                goto = 6
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 2
                else:raise # unhandled case, should not happen

        if goto == 2:
            w_1 = space.call_function(space.w_RuntimeError, gs_lost_sys_stdout)
            w_2 = space.type(w_1)
            w_3 = space.issubtype(w_2, space.w_type)
            v0 = space.is_true(w_3)
            if v0 == True:
                goto = 4
            else:
                goto = 3

        if goto == 3:
            w_4 = space.type(w_1)
            w_etype, w_evalue = w_4, w_1
            goto = 5

        if goto == 4:
            w_5 = space.call_function(w_1, )
            w_6 = space.type(w_5)
            w_etype, w_evalue = w_6, w_5
            goto = 5

        if goto == 5:
            raise gOperationError(w_etype, w_evalue)

        if goto == 6:
            return w_0

  fastf_sys_stdout = sys_stdout
  fastf_sys_stdout.__name__ = 'fastf_sys_stdout'

##SECTION##
## filename    'interpreter/pyopcode.py'
## function    'print_expr'
## firstlineno 1256
##SECTION##
# global declarations
# global object gs_displayhook
# global object gs_lost_sys_displayhook

  def print_expr(space, w_1):
    goto = 1 # startblock
    while True:

        if goto == 1:
            try:
                w_0 = space.getattr(mod_sys, gs_displayhook)
                goto = 5
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    goto = 2
                else:raise # unhandled case, should not happen

        if goto == 2:
            w_2 = space.call_function(space.w_RuntimeError, gs_lost_sys_displayhook)
            w_3 = space.type(w_2)
            w_4 = space.issubtype(w_3, space.w_type)
            v0 = space.is_true(w_4)
            if v0 == True:
                goto = 3
            else:
                goto = 4

        if goto == 3:
            w_5 = space.call_function(w_2, )
            w_6 = space.type(w_5)
            w_etype, w_evalue = w_6, w_5
            goto = 6

        if goto == 4:
            w_7 = space.type(w_2)
            w_etype, w_evalue = w_7, w_2
            goto = 6

        if goto == 5:
            w_8 = space.call_function(w_0, w_1)
            w_9 = space.w_None
            goto = 7

        if goto == 6:
            raise gOperationError(w_etype, w_evalue)

        if goto == 7:
            return w_9

  fastf_print_expr = print_expr
  fastf_print_expr.__name__ = 'fastf_print_expr'

##SECTION##
## filename    'interpreter/pyopcode.py'
## function    'print_item_to'
## firstlineno 1263
##SECTION##
# global declarations
# global object gs__
# global object gi_minus_1
# global object gs_isspace

  def print_item_to(space, w_1, w_stream):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = fastf_file_softspace(space, w_stream, space.w_False)
            v0 = space.is_true(w_0)
            if v0 == True:
                goto = 2
            else:
                goto = 3

        if goto == 2:
            w_2 = space.getattr(w_stream, gs_write)
            w_3 = space.call_function(w_2, gs__)
            goto = 3

        if goto == 3:
            w_4 = space.getattr(w_stream, gs_write)
            w_5 = space.str(w_1)
            w_6 = space.call_function(w_4, w_5)
            w_7 = space.isinstance(w_1, space.w_str)
            v1 = space.is_true(w_7)
            if v1 == True:
                goto = 4
            else:
                goto = 7

        if goto == 4:
            v2 = space.is_true(w_1)
            if v2 == True:
                goto = 5
            else:
                goto = 7

        if goto == 5:
            w_8 = space.getitem(w_1, gi_minus_1)
            w_9 = space.getattr(w_8, gs_isspace)
            w_10 = space.call_function(w_9, )
            v3 = space.is_true(w_10)
            if v3 == True:
                goto = 6
            else:
                goto = 7

        if goto == 6:
            w_11 = space.getitem(w_1, gi_minus_1)
            w_12 = space.ne(w_11, gs__)
            v4 = space.is_true(w_12)
            if v4 == True:
                w_13 = space.w_None
                goto = 8
            else:
                goto = 7

        if goto == 7:
            w_14 = fastf_file_softspace(space, w_stream, space.w_True)
            w_13 = space.w_None
            goto = 8

        if goto == 8:
            return w_13

  fastf_print_item_to = print_item_to
  fastf_print_item_to.__name__ = 'fastf_print_item_to'

##SECTION##
## filename    'interpreter/pyopcode.py'
## function    'print_item'
## firstlineno 1276
##SECTION##
  def print_item(space, w_x):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = fastf_sys_stdout(space, )
            w_1 = fastf_print_item_to(space, w_x, w_0)
            w_2 = space.w_None
            goto = 2

        if goto == 2:
            return w_2

  fastf_print_item = print_item
  fastf_print_item.__name__ = 'fastf_print_item'

##SECTION##
## filename    'interpreter/pyopcode.py'
## function    'print_newline_to'
## firstlineno 1280
##SECTION##
# global declarations
# global object gs_write
# global object gs__n

  def print_newline_to(space, w_stream):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = space.getattr(w_stream, gs_write)
            w_1 = space.call_function(w_0, gs__n)
            w_2 = fastf_file_softspace(space, w_stream, space.w_False)
            w_3 = space.w_None
            goto = 2

        if goto == 2:
            return w_3

  fastf_print_newline_to = print_newline_to
  fastf_print_newline_to.__name__ = 'fastf_print_newline_to'

##SECTION##
## filename    'interpreter/pyopcode.py'
## function    'print_newline'
## firstlineno 1284
##SECTION##
  def print_newline(space):
    goto = 1 # startblock
    while True:

        if goto == 1:
            w_0 = fastf_sys_stdout(space, )
            w_1 = fastf_print_newline_to(space, w_0)
            w_2 = space.w_None
            goto = 2

        if goto == 2:
            return w_2

  fastf_print_newline = print_newline
  fastf_print_newline.__name__ = 'fastf_print_newline'

##SECTION##
## filename    'interpreter/pyopcode.py'
## function    'file_softspace'
## firstlineno 1288
##SECTION##
# global declarations
# global object g11dict
# global object gs_print_item_to
# global object gfunc_print_item_to
# global object gs_print_newline
# global object gfunc_print_newline
# global object gs___file__
# global object gs__Users_steve_Documents_MIT_TPP_2
# global object gs_sys_stdout
# global object gfunc_sys_stdout
# global object gs_print_expr
# global object gfunc_print_expr
# global object gs_sys
# global object mod_sys
# global object bltinmod_helper
# global object gs_print_item
# global object gfunc_print_item
# global object gs_print_newline_to
# global object gfunc_print_newline_to
# global object gs___name__
# global object gs___builtin__
# global object gs_file_softspace
# global object gfunc_file_softspace
# global object gs_softspace
# global object gi_0

  def file_softspace(space, w_1, w_3):
    goto = 1 # startblock
    while True:

        if goto == 1:
            try:
                w_0 = space.getattr(w_1, gs_softspace)
                w_2 = w_0
                goto = 2
            except gOperationError, e:
                e.normalize_exception(space)
                if e.match(space, space.w_AttributeError):
                    w_2 = gi_0
                    goto = 2
                else:raise # unhandled case, should not happen

        if goto == 2:
            w_4 = space.setattr(w_1, gs_softspace, w_3)
            goto = 3

        if goto == 3:
            return w_2

  fastf_file_softspace = file_softspace
  fastf_file_softspace.__name__ = 'fastf_file_softspace'

##SECTION##
  g11dict = space.newdict()
  gs_print_item_to = space.new_interned_str('print_item_to')
  from pypy.interpreter import gateway
  gfunc_print_item_to = space.wrap(gateway.interp2app(fastf_print_item_to, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g11dict, gs_print_item_to, gfunc_print_item_to)
  gs_print_newline = space.new_interned_str('print_newline')
  gfunc_print_newline = space.wrap(gateway.interp2app(fastf_print_newline, unwrap_spec=[gateway.ObjSpace, ]))
  space.setitem(g11dict, gs_print_newline, gfunc_print_newline)
  gs___file__ = space.new_interned_str('__file__')
  gs__Users_steve_Documents_MIT_TPP_2 = space.new_interned_str(
"""/Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/interpreter/pyopcode.py""")
  space.setitem(g11dict, gs___file__, gs__Users_steve_Documents_MIT_TPP_2)
  gs_sys_stdout = space.new_interned_str('sys_stdout')
  gfunc_sys_stdout = space.wrap(gateway.interp2app(fastf_sys_stdout, unwrap_spec=[gateway.ObjSpace, ]))
  space.setitem(g11dict, gs_sys_stdout, gfunc_sys_stdout)
  gs_print_expr = space.new_interned_str('print_expr')
  gfunc_print_expr = space.wrap(gateway.interp2app(fastf_print_expr, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g11dict, gs_print_expr, gfunc_print_expr)
  gs_sys = space.new_interned_str('sys')
  def bltinmod_helper(name):
      dic = space.newdict()
      space.exec_("import %s" % name, dic, dic, hidden_applevel=True)
      return space.eval("%s" % name, dic, dic, hidden_applevel=True)
  mod_sys = bltinmod_helper('sys')
  space.setitem(g11dict, gs_sys, mod_sys)
  gs_print_item = space.new_interned_str('print_item')
  gfunc_print_item = space.wrap(gateway.interp2app(fastf_print_item, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g11dict, gs_print_item, gfunc_print_item)
  gs_print_newline_to = space.new_interned_str('print_newline_to')
  gfunc_print_newline_to = space.wrap(gateway.interp2app(fastf_print_newline_to, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g11dict, gs_print_newline_to, gfunc_print_newline_to)
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g11dict, gs___name__, gs___builtin__)
  gs_file_softspace = space.new_interned_str('file_softspace')
  gfunc_file_softspace = space.wrap(gateway.interp2app(fastf_file_softspace, unwrap_spec=[gateway.ObjSpace, gateway.W_Root, gateway.W_Root]))
  space.setitem(g11dict, gs_file_softspace, gfunc_file_softspace)
  gs_softspace = space.new_interned_str('softspace')
  from pypy.interpreter.error import OperationError as gOperationError
  gi_0 = space.wrap(0)
  gs_write = space.new_interned_str('write')
  gs__n = space.new_interned_str(
"""
""")
  gs_displayhook = space.new_interned_str('displayhook')
  gs_lost_sys_displayhook = space.new_interned_str('lost sys.displayhook')
  gs_stdout = space.new_interned_str('stdout')
  gs_lost_sys_stdout = space.new_interned_str('lost sys.stdout')
  gs__ = space.new_interned_str(' ')
  gi_minus_1 = space.wrap(-1)
  gs_isspace = space.new_interned_str('isspace')
  return g11dict


from pypy._cache import known_code
known_code['77fe4d1b6e496ab15705292ceb905ea8'] = init__builtin__
