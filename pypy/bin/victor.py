import inspect, sys
import copy
def trace(f,e,a):
    if e == 'return':
        output = "RETURN " + str(a) + "(" + f.f_code.co_name
        co = f.f_code
        if len(co.co_filename) > 75:
            fname = co.co_filename[80:]
        else:
            fname = co.co_filename
        output += " " + fname + " " + co.co_firstlineno + ")"
        print output
    if e == 'call':
        co = f.f_code
        if len(co.co_filename) > 75:
            fname = co.co_filename[80:]
        else:
            fname = co.co_filename
        args = inspect.getargvalues(f)
        callee = ""
        if len(args[0]) > 0:
            if hasattr(args[3][args[0][0]],'__class__'):
                callee = str(args[3][args[0][0]].__class__)
        values = ""
        try:
            values = str(args[3])
        except Exception, e:
            pass
        output = co.co_name + "(" + str(args[0]) + ")" + "(" + values + ") " + fname + " " + str(co.co_firstlineno)
        if f.f_back is not None:
            co = f.f_back.f_code
            if len(co.co_filename) > 75 and co.co_filename.find("sourcetools.py") == -1:
                fname = co.co_filename[80:]
            else:
                fname = co.co_filename
            args = inspect.getargvalues(f.f_back)
            caller = ""
            if len(args[0]) > 0:
                if hasattr(args[3][args[0][0]],'__class__'):
                    caller = str(args[3][args[0][0]].__class__)
                else:
                    caller = str(type(args[3][args[0][0]]))
            output += " " + co.co_name + "(" + caller + ") " + fname + " " + str(co.co_firstlineno)
        print output

def hello():
    pow(2,3)


def bad():
    print badarg

def ev():
    inspect.getmembers(eval) 

dnewtypes = {}
dnotypes = {}
dnewobjs = {}
doldobjs = {}
dobjlevels = {}
depthreached = 0

def dcop(obj,depth):
    global dnewtypes
    global dnotypes
    global dnewobjs
    global depthreached
    global doldobjs
    global dobjlevels
    
    dnewtypes = {}
    dnotypes = {}
    dnewobjs = {}
    doldobjs = {}
    dobjlevels = {}
    depthreached = 0
    new = obj
    try:
        new = copy.copy(obj)
        assert id(new) != id(obj)
    except Exception, e:
        print e, type(e)
    except AssertionError, e:
        print e, type(e)
    else:
        doldobjs[id(obj)] = new
        dnewobjs[id(new)] = new
        dnewtypes[type(new).__name__] = type(new)
        for r in range(0,depth):
            dcoph(new,r)
            print r, len(dnewobjs)
    return new

def fdcop(obj,depth):
    global dnewtypes
    global dnotypes
    global dnewobjs
    global depthreached
    global doldobjs
    global dobjlevels
    
    dnewtypes = {}
    dnotypes = {}
    dnewobjs = {}
    doldobjs = {}
    dobjlevels = {}
    depthreached = 0
    new = obj
    try:
        new = copy.copy(obj)
        assert id(new) != id(obj)
    except Exception, e:
        print e, type(e)
    except AssertionError, e:
        print e, type(e)
    else:
        doldobjs[id(obj)] = new
        dnewobjs[id(new)] = new
        dnewtypes[type(new).__name__] = type(new)
        for r in range(0,depth):
            fdcoph(new,r)
            #print r, len(dnewobjs)
    return new

def dcophatt(obj,name,att):
    aco = att
    if doldobjs.has_key(id(att)) or dnewobjs.has_key(id(att)): 
        if doldobjs.has_key(id(att)):
            aco = doldobjs[id(att)]
        else:
            aco = dnewobjs[id(att)]
        # Take care that dict type keys don't cl
        try:
            t = type(obj).__name__
            if dobjlevels[id(obj)] == depthreached-1 and hasattr(obj,name):
                setattr(obj,name,aco)
        except Exception, e:
            pass
        return aco
    
    t = type(obj).__name__
    try:
        aco = copy.copy(att)
        assert id(aco) != id(att)
        doldobjs[id(att)] = aco
        dnewobjs[id(aco)] = aco
        dobjlevels[id(aco)] = depthreached
        dnewtypes[type(aco).__name__] = type(aco)
        if hasattr(obj,name):
            setattr(obj,name,aco)
        #print type(obj), id(obj), name, type(att)
    except AssertionError, e:
        if not dnotypes.has_key(type(att).__name__):
            dnotypes[t+'_'+name+'_'+type(att).__name__] = {}
        dnotypes[t+'_'+name+'_'+type(att).__name__][str(e)] = type(e)
    except AttributeError, e:
        if str(e).find('read-only') == -1 and str(e).find('not writable') == -1 and str(e).find('unknown option') == -1:
            if not dnotypes.has_key(type(att).__name__):
                dnotypes[t+'_'+name+'_'+type(att).__name__] = {}
            dnotypes[t+'_'+name+'_'+type(att).__name__][str(e)] = type(e)
    except TypeError, e:
        if str(e).find('readonly') == -1: 
            if not dnotypes.has_key(type(att).__name__):
                dnotypes[t+'_'+name+'_'+type(att).__name__] = {}
            dnotypes[t+'_'+name+'_'+type(att).__name__][str(e)] = type(e) 
    except Exception, e:
        po = obj
        atto = att
        if t == 'dict' or t == 'list':
            po = str(len(obj))
        at = type(att).__name__
        if at == 'dict' or at == 'list':
            atto = len(att)
        print po, type(obj), name+"="+str(atto),e, type(e), level
    return aco

def dcoph(obj,depth,level=0):
    global depthreached
    if level > depthreached:
        depthreached = level
    l = None
    try:
        l = inspect.getmembers(obj)
    except Exception, e:
        # These exceptions are out of my control
        return
    if level == depth:
        adict = None
        if hasattr(obj,'__dict__') and not id(obj) in dnewobjs:
            adict_t = obj.__dict__
            if type(adict_t).__name__ == 'dict':
                adict = dcophatt(obj,'__dict__',adict_t)
        for att in l:
            if att[0] == 'content' or att[0] == 'w_dict' or att[0] == '_dict' or att[0] == 'w_func_globals' or att[0] == 'w_class' or att[0] == 'wrappeditems':
                t = type(att[1]).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    dcophatt(obj,att[0],att[1])
        t = type(obj).__name__
        if t == 'dict':
            for k,elt in obj.iteritems():
                t = type(elt).__name__
                newelt = None
                newkey = None
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    t = type(k).__name__
                    if t == 'dict' or t == 'set' or t == 'list' or t == 'buffer' or str(type(obj)).find('collections.') != -1:
                        n = "key="+type(k).__name__
                    else:
                        n = "key="+str(k)
                    newelt = dcophatt(obj,n,elt)
                t = type(k).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    newkey = dcophatt(obj,'isadictkey',k)
                if newelt is not None and newkey is not None:
                    obj.pop(k)
                    obj[newkey] = newelt
                elif newelt is not None:
                    obj[k] = newelt
                elif newkey is not None:
                    obj.pop(k)
                    obj[newkey] = elt
        if t == 'set' or t == 'list' or t == 'buffer' or str(type(obj)).find('collections.') != -1:
            for i,elt in enumerate(obj):
                t = type(elt).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    obj[i] = dcophatt(obj,"seqtype_"+str(i),elt)
    elif level < depth:
        for att in l:
            t = type(att[1]).__name__
            if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(att[1]) in dnewobjs:
                dcoph(att[1],depth,level+1)
        t = type(obj).__name__
        if t == 'dict':
            for k,elt in obj.iteritems():
                t = type(elt).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(elt) in dnewobjs:
                    dcoph(elt,depth,level+1)
                t = type(k).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(k) in dnewobjs:
                    dcoph(k,depth,level+1)
        if t == 'set' or t == 'list' or t == 'buffer' or str(type(obj)).find('collections.') != -1:
            for elt in obj:
                t = type(elt).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(elt) in dnewobjs:
                    dcoph(elt,depth,level+1)
    else:
        raise Exception("none or too many levels")

def fdcoph(obj,depth,level=0):
    global depthreached
    if level > depthreached:
        depthreached = level
    l = None
    try:
        l = inspect.getmembers(obj)
    except Exception, e:
        #Nothing we can do here
        return
    if level == depth:
        adict = None
        if hasattr(obj,'__dict__') and not id(obj) in dnewobjs:
            adict_t = obj.__dict__
            if type(adict_t).__name__ == 'dict':
                adict = dcophatt(obj,'__dict__',adict_t)
        for att in l:
            if (att[0] == 'content' or att[0] == 'w_dict' or att[0] == '_dict' or att[0] == 'w_func_globals' or att[0] == 'w_class' or att[0] == 'wrappeditems' or att[0] == 'key'):
                t = type(att[1]).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    dcophatt(obj,att[0],att[1])
        t = type(obj).__name__
        if t == 'dict':
            for k,elt in obj.iteritems():
                newkey = None
                newelt = None
                tk = type(k).__name__
                n = "key="+str(k)
                if tk == '_r_dictkey':
                    t = type(k.key).__name__
                else:
                    t = type(k).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    newkey = dcophatt(obj,'isadictkey',k)
                    
                t = type(elt).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    n = "key="+str(k)
                    newelt = dcophatt(obj,n,elt)
                if newelt is not None and newkey is not None:
                    obj.pop(k)
                    obj[newkey] = newelt
                elif newelt is not None:
                    obj[k] = newelt
                elif newkey is not None:
                    obj.pop(k)
                    obj[newkey] = elt
        if t == 'set' or t == 'list' or t == 'buffer' or str(type(obj)).find('collections.') != -1:
            for i,elt in enumerate(obj):
                t = type(elt).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
                    obj[i] = dcophatt(obj,"seqtype_"+str(i),elt)
    elif level < depth:
        for att in l:
            t = type(att[1]).__name__
            if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(att[1]) in dnewobjs:
                fdcoph(att[1],depth,level+1)
        t = type(obj).__name__
        if t == 'dict':
            for k,elt in obj.iteritems():
                t = type(elt).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(elt) in dnewobjs:
                    fdcoph(elt,depth,level+1)
                t = type(k).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(k) in dnewobjs:
                    fdcoph(k,depth,level+1)
        if t == 'set' or t == 'list' or t == 'buffer' or str(type(obj)).find('collections.') != -1:
            for elt in obj:
                t = type(elt).__name__
                if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod') and id(elt) in dnewobjs:
                    fdcoph(elt,depth,level+1)
    else:
        raise Exception("none or too many levels")

newtypes = {}
notypes = {}
newobjs = {}
def cop(obj,limit=0,level=0):
    new = obj
    if limit and level > limit: 
        return new
    if newobjs.has_key(id(obj)):
        return newobjs[id(obj)]
    name = ''
    numargs = 1
    if hasattr(obj,'__name__'):
        name = obj.__name__
    if hasattr(obj,'__init__'):
        pass
        #numargs = len(obj.__init__.im_func.func_code.co_varnames)
    t = type(obj).__name__
    if (t != 'object' and t != 'type' and t != 'str' and t != 'NoneType' and t != 'builtin_function_or_method' and t != 'float' and t != 'int' and t != 'code' and t != 'bool' and t != 'method-wrapper' and t != 'instancemethod'):
        new = copy.copy(obj)
        newobjs[id(new)] = new
        newtypes[type(new).__name__] = type(new)
        l = inspect.getmembers(obj)
        for att in l:
            try:
                setattr(new,att[0],cop(att[1],limit,level+1))
            except AttributeError, e:
                if str(e).find('read-only') == -1 and str(e).find('not writable') == -1 and str(e).find('unknown option') == -1:
                    if not notypes.has_key(type(att[1]).__name__):
                        notypes[t+'_'+att[0]+'_'+type(att[1]).__name__] = {}
                    notypes[t+'_'+att[0]+'_'+type(att[1]).__name__][str(e)] = type(e)
            except TypeError, e:
                if str(e).find('readonly') == -1: 
                    if not notypes.has_key(type(att[1]).__name__):
                        notypes[t+'_'+att[0]+'_'+type(att[1]).__name__] = {}
                    notypes[t+'_'+att[0]+'_'+type(att[1]).__name__][str(e)] = type(e) 
            except Exception, e:
                po = obj
                atto = att[1]
                if t == 'dict' or t == 'list':
                    po = str(len(obj))
                at = type(att[1]).__name__
                if at == 'dict' or at == 'list':
                    atto = len(att[1])
                print po, type(obj), att[0]+"="+str(atto),e, type(e), level
    newobjs[id(obj)] = new
    return new

def tcop(obj):
    new = obj
    try:
        new = copy.copy(obj)
    except Exception, e:
        print "copy(obj):", obj, type(obj), e, type(e)
    else:
        l = inspect.getmembers(obj)
        for att in l:
            try:
                catt = copy.copy(att[1])
            except Exception, e:
                print "copy(att[1]):", obj, type(obj), att[0]+"="+str(att[1]),e, type(e)
            else:
                try:
                    setattr(new,att[0],catt)
                except Exception, e:
                    print "setattr(att[0]):", obj, type(obj), att[0]+"="+str(att[1]),e, type(e)
                else:
                    print "setattr", att[0], "success"
    return new

def fcop(obj):
    l = inspect.getmembers(obj)
    for att in l:
        try:
            setattr(obj,att[0],att[1])
        except Exception, e:
            if type(att[1]).__name__ == 'list' or type(att[1]).__name__ == 'dict':
                atto = len(att[1])
            else:
                atto = att[1]
            print "setattr(att[0]):", att[0]+"="+str(atto), e, type(e)
        else:
            print "setattr", att[0], "success"

def rfcop(obj,depth=0):
    for r in range(0,depth):
        rfcoph(obj,r)


def rfcoph(obj,depth=0,level=0):
    l = inspect.getmembers(obj)
    if level == depth:
        for att in l:
            try:
                setattr(obj,att[0],att[1])
            except Exception, e:
                if type(att[1]).__name__ == 'list' or type(att[1]).__name__ == 'dict':
                    atto = len(att[1])
                else:
                    atto = att[1]
            #print "setattr(att[0]):", att[0]+"="+str(atto), e, type(e)
            else:
                if not (att[0] == '__module__' and att[1] == None):
                    print "setattr", att[0], "success", type(obj), level
    elif level < depth:
        for att in l:
            rfcoph(att[1],depth,level+1)

def printypes(obj):
    l = inspect.getmembers(obj)
    out = ""
    for att in l:
        out += type(att[1]).__name__ + " "
    print out


def prof(str):
    import cProfile
    cProfile.run(str)

def test(w_mod,level,i1,i2):
    c = fdcop(w_mod,level)
    k = w_mod.w_dict.content._dict.keys()[i1]
    m = w_mod.w_dict.content._dict.values()[i2]
    cm = fdcop(m,0)
    c.w_dict.content._dict[k] = cm
    print id(cm)
    return c
