#
#  namespace.py
#  pypy_xcode
#
#  Created by Stephen Woodrow on 06/12/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

from pypy.interpreter import gateway, buffer
from pypy.interpreter.baseobjspace import ObjSpace
from pypy.interpreter.error import OperationError
from pypy.rlib.runicode import UNICHR
import __builtin__
NoneNotWrapped = gateway.NoneNotWrapped

Buffer = buffer.Buffer

def newtoken(space):
    from pypy.objspace.std.nametokenobject import W_NametokenObject
    return W_NametokenObject()
    
def changetoken(space,w_obj,w_token):
    if id(w_obj) in space.namespace_table:
        space.namespace_table[id(w_obj)] = w_token
        return True
    else:
        return False