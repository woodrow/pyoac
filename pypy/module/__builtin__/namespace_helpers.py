#
#  namespace_helpers.py
#  pypy

from pypy.interpreter.baseobjspace import W_Root, ObjSpace
from pypy.interpreter.error import OperationError

# "constants"
SLOTNAME_ALLTOKENS = "__alltokens__"
SLOTNAME_NAMETOKEN = "__nametoken__"

# if false, throw "not found" exceptions and return None
# if true, throw access exceptions
# ALSO: change in nestedscope.py
throw_access_exceptions = False ##DO NOT set = True -- this will break lots of stuff!
print_access_exceptions = True

def _currentframe_has_access(space, w_obj):
    """Return a boolean result about whether the current frame has access to the given object"""
    try:
        w_objtoken = space.namespace_table[id(w_obj)]
    except KeyError:
        return True #!!!: this means that an object with no token is open -- this seems reasonable for functionality's sake
    
    try: # check against __nametoken__
        w_frameglobals_nametoken = space.getitem(space.getexecutioncontext().framestack.top().w_globals, space.wrap(SLOTNAME_NAMETOKEN))
        if space.is_w(w_objtoken, w_frameglobals_nametoken):
            return True
    except OperationError, e:
        if not e.match(space, space.w_KeyError):
            raise
    
    try: # check against __alltokens__
        w_frameglobals_alltokens = space.getitem(space.getexecutioncontext().framestack.top().w_globals, space.wrap(SLOTNAME_ALLTOKENS))
        return w_objtoken in space.unpackiterable(space.call_function(space.getattr(w_frameglobals_alltokens,space.wrap("values"))))
    except OperationError, e:
 #       if not e.match(space, space.w_KeyError):
 #           raise
        return False
 #   return False