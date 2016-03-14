README
======
If you have any problems, please contact woodrow@mit.edu.


APPLYING OUR PATCH
------------------

To apply our patch to Pypy:

1. Checkout r69315 from the pypy repo:
    % svn co -r 69315 http://codespeak.net/svn/pypy/dist pypy-dist

2. Apply our patch (I had the best luck making the patch with git -- hopefully
   you have it):
    % git apply /path/to/pypy.patch
    
    NOTE that Pypy DOES NOT need to be in a git repo for this to work

3. You should be good to go. You can run the pypy interpreter as follows:
    % cd pypy-dist/pypy
    % python bin/py.py
    
    PLEASE NOTE: pypy doesn't appear to work with Python 2.6. Please use Python 2.5.
    

TRYING OUT OUR MODIFICATIONS
----------------------------

> A demo of the object copying features are available by following the example 
    in project report.

> A demo of the access control and proxy object capabilities are available by
    running:
    
    % python bin/py.py nametest.py **NOTE this will access documents in /tmp**
    
    nametest.py in turn works with nametest_trust.py and nametest_notrust.py.
    
    To see what's going on "under the covers" and in particular the object-token
    mapping table, hit ctrl-c to drop into the CPython interpreter beneath Pypy
    and look at space.namespace_table. Token objects can't be examined directly,
    but may be distinguished by their unique id()s. Hit ctrl-d to return to Pypy.
    
    Some key functions:
    
    token = newtoken("token_identifier_string")
    changetoken(object, token)
    set_nametoken(token)
    moduleobj = __import__("modulename", globals(), {"__nametoken__": token})

    Some key globals objects (remember to use globals keyword to modify these)
    __nametoken__ = token
    __alltokens__ = {"token_identifier_string": token, ...}
    
    Remember that when operating interactively, to attempt to exclude yourself 
    from a particular namespace in case you just want to "see what happens", you
    must remove its token from both __nametoken__ and __alltokens__.
    

CAVEATS
-------
Our copying and access control mechanisms haven't been tested simultaneously, and so it is
not clear what the consequences of attempting to use the mechanisms together might be. We
recommend testing them individually.

Also, imports under the access control system, once __nametoken__ is set, may 
cause import failures in other namespaces for the same module or modules dependent on
the initially imported module. This is due to Python's sharing of module implementations
internally, which is incompatible with the idea of partitioned namespaces. In other words
the first namespace that imports a module "lays claim" to it with its token,
preventing it from being imported by other namespaces. 