"""
Version numbers exposed by PyPy through the 'sys' module.
"""
import os


CPYTHON_VERSION            = (2, 5, 2, "beta", 42)
CPYTHON_API_VERSION        = 1012

# release 1.1.0
PYPY_VERSION               = (1, 1, 0, "beta", '?')
# the last item is replaced by the svn revision ^^^

TRIM_URL_UP_TO = 'svn/pypy/'
SVN_URL = "$HeadURL: http://codespeak.net/svn/pypy/dist/pypy/module/sys/version.py $"[10:-28]

REV = "$LastChangedRevision: 64770 $"[22:-2]


import pypy
pypydir = os.path.dirname(os.path.abspath(pypy.__file__))
del pypy

import time as t
gmtime = t.gmtime()
date = t.strftime("%b %d %Y", gmtime)
time = t.strftime("%H:%M:%S", gmtime)
del t

# ____________________________________________________________

def get_api_version(space):
    return space.wrap(CPYTHON_API_VERSION)

def get_version_info(space):
    return space.wrap(CPYTHON_VERSION)

def get_version(space):
    return space.wrap("%d.%d.%d (%d, %s, %s)\n[PyPy %d.%d.%d]" % (
        CPYTHON_VERSION[0],
        CPYTHON_VERSION[1],
        CPYTHON_VERSION[2],
        svn_revision(),
        date,
        time,
        PYPY_VERSION[0],
        PYPY_VERSION[1],
        PYPY_VERSION[2]))

def get_hexversion(space):
    return space.wrap(tuple2hex(CPYTHON_VERSION))

def get_pypy_version_info(space):
    ver = PYPY_VERSION
    ver = ver[:-1] + (svn_revision(),)
    return space.wrap(ver)

def get_svn_url(space):
    return space.wrap((SVN_URL, svn_revision()))

def get_subversion_info(space):
    svnbranch = SVN_URL
    if TRIM_URL_UP_TO in svnbranch:
        svnbranch = svnbranch.split(TRIM_URL_UP_TO, 1)[1]
    svnbranch = svnbranch.strip('/')
    return space.newtuple([space.wrap('PyPy'),
                           space.wrap(svnbranch),
                           space.wrap(str(svn_revision()))])

def tuple2hex(ver):
    d = {'alpha':     0xA,
         'beta':      0xB,
         'candidate': 0xC,
         'final':     0xF,
         }
    subver = ver[4]
    if not (0 <= subver <= 9):
        subver = 0
    return (ver[0] << 24   |
            ver[1] << 16   |
            ver[2] << 8    |
            d[ver[3]] << 4 |
            subver)

def svn_revision():
    "Return the last-changed svn revision number."
    # NB. we hack the number directly out of the .svn directory to avoid
    # to depend on an external 'svn' executable in the path.
    rev = int(REV)
    try:
        f = open(os.path.join(pypydir, '.svn', 'format'), 'r')
        format = int(f.readline().strip())
        f.close()
        if format <= 6: # Old XML-format
            f = open(os.path.join(pypydir, '.svn', 'entries'), 'r')
            for line in f:
                line = line.strip()
                if line.startswith('committed-rev="') and line.endswith('"'):
                    rev = int(line[15:-1])
                    break
            f.close()
        else: # New format
            f = open(os.path.join(pypydir, '.svn', 'entries'), 'r')
            format = int(f.readline().strip())
            for entry in f.read().split('\f'):
                lines = entry.split('\n')
                name, kind, revstr = lines[:3]
                if name == '' and kind == 'dir': # The current directory
                    rev = int(revstr)
                    break
            f.close()
    except (IOError, OSError):
        pass
    return rev
