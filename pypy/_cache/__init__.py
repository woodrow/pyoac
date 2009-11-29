# This folder acts as a cache for code snippets which have been
# compiled by compile_as_module().
# It will get a new entry for every piece of code that has
# not been seen, yet.
#
# Caution! Only the code snippet is checked. If something
# is imported, changes are not detected. Also, changes
# to geninterplevel or gateway are also not checked.
# Exception: There is a checked version number in geninterplevel.py
#
# If in doubt, remove this file from time to time.

GI_VERSION_RENDERED = '1.1.26'

known_code = {}

# self-destruct on double-click:
def harakiri():
    import pypy._cache as _c
    import py
    lp = py.path.local
    for pth in lp(_c.__file__).dirpath().listdir():
        try:
            pth.remove()
        except: pass

if __name__ == "__main__":
    harakiri()

del harakiri
