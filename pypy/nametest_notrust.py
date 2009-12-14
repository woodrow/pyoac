myname = __name__ + " (nametest_notrust.py)"
print("\n"*2 + myname + "\n" + "="*len(myname))

print("id(globals.__nametoken__)=" + str(id(__nametoken__)))

def filewrite(open_func):
    print("\n" + ">>>> filewrite(open_func):")
    f = open_func("notrust.txt", "w")
    f.write(str(id(__nametoken__)) + "-untrusted.\n")
    f.close()
    print("untrusted module wrote file to /tmp/notrust.txt")
    print("\n" + "NOW, let's look inside...")
    print("open_func.func_closure: " + str(open_func.func_closure))
    
    if open_func.func_closure is not None:
        for obj in open_func.func_closure:
            print(" "*2+str(obj)+".cell_contents: " + str(obj.cell_contents))
            print(" "*2+"id("+str(obj)+".cell_contents): " + str(id(obj.cell_contents)))

    #compare with __builtins__.open, which is currently unrestricted -- this would need to be dealt with in future
    print("\n" + "__builtins__.open: " + str(__builtins__.open))
    print("id(__builtins__.open): " + str(id(__builtins__.open)))

    print("\n" + "open_func.func_code: " + str(open_func.func_code))
    
def getsecrets():
    print("\n" + ">>>> getsecrets():")
    import sys
    try:
        print("""sys.modules["nametest"].__dict__["_nametest_secret"]: """ + str(sys.modules["nametest"].__dict__["_nametest_secret"]))
    except KeyError:
        try:
            print("""sys.modules["__main__"].__dict__["_nametest_secret"]: """ + str(sys.modules["__main__"].__dict__["_nametest_secret"]))
        except KeyError:
            print("couldn't access '_nametest_secret'")
            
    try:
        print("""sys.modules["nametest_trust"].__dict__["_nametest_trust_secret"]: """ + str(sys.modules["nametest_trust"].__dict__["_nametest_trust_secret"]))
    except KeyError:
        print("couldn't access '_nametest_trust_secret'")
            
    
    