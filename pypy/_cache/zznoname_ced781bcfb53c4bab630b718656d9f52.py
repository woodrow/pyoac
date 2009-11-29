# self-destruct on double-click:
if __name__ == "__main__":
    from pypy import _cache
    import os
    namestart = os.path.join(os.path.split(_cache.__file__)[0], 'zznoname_ced781bcfb53c4bab630b718656d9f52')
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
## filename    '<codegen /Users/steve/Documents/MIT TPP/2009-2010/6.893/project/pypy-dist/pypy/interpreter/gateway.py:824>'
## function    'pypy_init'
## firstlineno 2
##SECTION##
# global declarations
# global object g3dict
# global object gs___name__
# global object gs___builtin__
# global object gs_pypy_init
# global object gfunc_pypy_init
# global object gs___import__
# global object gs_site
# global object g0dict

  def pypy_init(space, w_import_site):
    goto = 1 # startblock
    while True:

        if goto == 1:
            v0 = space.is_true(w_import_site)
            if v0 == True:
                goto = 2
            else:
                w_0 = space.w_None
                goto = 3

        if goto == 2:
            w_1 = space.call_function((space.builtin.get(space.str_w(gs___import__))), gs_site, g0dict, space.w_None, space.w_None)
            w_0 = space.w_None
            goto = 3

        if goto == 3:
            return w_0

  fastf_pypy_init = pypy_init
  fastf_pypy_init.__name__ = 'fastf_pypy_init'

##SECTION##
  g3dict = space.newdict()
  gs___name__ = space.new_interned_str('__name__')
  gs___builtin__ = space.new_interned_str('__builtin__')
  space.setitem(g3dict, gs___name__, gs___builtin__)
  gs_pypy_init = space.new_interned_str('pypy_init')
  from pypy.interpreter import gateway
  gfunc_pypy_init = space.wrap(gateway.interp2app(fastf_pypy_init, unwrap_spec=[gateway.ObjSpace, gateway.W_Root]))
  space.setitem(g3dict, gs_pypy_init, gfunc_pypy_init)
  gs___import__ = space.new_interned_str('__import__')
  gs_site = space.new_interned_str('site')
  g0dict = space.newdict()
  return g3dict


from pypy._cache import known_code
known_code['ced781bcfb53c4bab630b718656d9f52'] = init__builtin__
