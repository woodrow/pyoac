#
#  namespace.py
#  pypy_xcode
#
#  Created by Stephen Woodrow on 06/12/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

from pypy.objspace.std.nametokenobject import W_NametokenObject
from pypy.interpreter import gateway, buffer
from pypy.interpreter.baseobjspace import ObjSpace
from pypy.objspace.std import StdObjSpace
from pypy.interpreter.error import OperationError
from pypy.rlib.runicode import UNICHR
import __builtin__
from pypy.module.__builtin__.namespace_helpers import SLOTNAME_ALLTOKENS, SLOTNAME_NAMETOKEN, _currentframe_has_access

NoneNotWrapped = gateway.NoneNotWrapped
Buffer = buffer.Buffer

def newtoken(space, w_tokenkey_str):
    w_newtok = W_NametokenObject()
    _changetoken(space,w_newtok,w_newtok) # make self-owned

    try: # get reference to __alltokens__ from frame globals
        w_frameglobals_alltokens = space.getitem(space.getexecutioncontext().framestack.top().w_globals, space.wrap(SLOTNAME_ALLTOKENS))
    except OperationError, e:
        if e.match(space, space.w_KeyError):
            w_frameglobals_alltokens = space.newdict() # instantiate __alltokens__
            space.set_str_keyed_item(space.getexecutioncontext().framestack.top().w_globals, space.wrap(SLOTNAME_ALLTOKENS), w_frameglobals_alltokens)
            #w_frameglobals_alltokens = space.getitem(space.getexecutioncontext().framestack.top().w_globals, space.wrap(SLOTNAME_ALLTOKENS))
        else:
            raise
    finally:
        space.set_str_keyed_item(w_frameglobals_alltokens, w_tokenkey_str, w_newtok)
            
    return w_newtok
    
    
def changetoken(space,w_obj,w_token):
    # ASSUMPTION: if caller can pass a reference to w_token, it has permission to use it
    # check that w_obj is NOT a nametoken object (don't allow a token to change it's self-ownership)
    if isinstance(w_obj, W_NametokenObject):
        return space.w_False
    # check that w_token is a nametoken object
    if not isinstance(w_token, W_NametokenObject):
        return space.w_False
    # check that the caller has permission to change
    if not _currentframe_has_access(space, w_obj):
        return space.w_False
    _changetoken(space, w_obj, w_token)
    return space.w_True
        
def _changetoken(space, w_obj, w_token):
    """Internal (interp-level) implementation of changetoken that doesn't check the existing owner -- use this wisely"""
    try:
        space.namespace_table[id(w_obj)] = w_token
    except NameError or TypeError: # space.namespace_table not yet instantiated
        space.namespace_table = {}
        space.namespace_table[id(w_obj)] = w_token
       
def set_nametoken(space, w_token):
    # assume that caller has access to w_token by virtue of being able to get it on the stack
    # check that w_token is a nametoken object
    if not isinstance(w_token, W_NametokenObject):
        return space.w_False
    space.setitem(space.getexecutioncontext().framestack.top().w_globals, space.wrap(SLOTNAME_NAMETOKEN), w_token)
    return space.w_True
