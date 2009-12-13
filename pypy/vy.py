import sys, vtrust

def destroy():
    #print dir()
    #print id(globals()['sys'])
    #print id(sys)
    #print locals()
    sys.version = "gotcha!"
    sys.stdin = None
    print "trying to destroy your env."

def evil():
    print "sneaky eval"
    r = eval('1+2')
    print r

def destroyout():
    print "setting stdout to None!"
    sys.stdout = None

def hurtvtrust():
    vtrust.c.l.append(4)
    vtrust.c.t = ()
    vtrust.i1.trick = "tricked you!"
    print "Erase vtrust.c.t, append to vtrust.c.l, insert 'trick' attribute to i1."
