from pypy.objspace.std.objspace import *


class W_NametokenObject(W_Object):
    """Instances of this class are what the user can directly see with an
    'object()' call."""
    from pypy.objspace.std.nametokentype import nametoken_typedef as typedef

# ____________________________________________________________


register_all(vars())
