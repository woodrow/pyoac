#
#  namespace.py
#  pypy_xcode
#
#  Created by Stephen Woodrow on 06/12/09.
#  Copyright (c) 2009 __MyCompanyName__. All rights reserved.
#

def newtoken():
    from pypy.objspace.std.nametokenobject import W_NametokenObject
    return W_NametokenObject()
    
def changetoken(space,w_obj,w_token):
    if id(w_obj) in space.namespace_table:
        space.namespace_table[id(w_obj)] = w_token
        return True
    else:
        return False