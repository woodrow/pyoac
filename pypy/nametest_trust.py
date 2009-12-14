myname = __name__ + " (nametest_trust.py)"
print("\n"*2 + myname + "\n" + "="*len(myname))

def restricted_open(f_open, basepath):
    def ropen(filename, mode='r', bufsize=-1):
        from os import path
        rpath = path.join(basepath, path.normpath(filename))
        return f_open(rpath, mode, bufsize)
    return ropen

trusted_token = newtoken("trusted")
print("id(trusted_token)=" + str(id(trusted_token)))
set_nametoken(trusted_token)
print("id(globals.__nametoken__)=" + str(id(__nametoken__)))
untrusted_token = newtoken("untrusted")
print("id(untrusted_token)=" + str(id(untrusted_token)))

_nametest_trust_secret = "Mum's the word."

ropen_tester = restricted_open(open,"/tmp")
f = ropen_tester("trusted.txt", "w")
f.write(str(id(__nametoken__)) + "-trusted.\n")
f.close()
print("trusted module wrote file to /tmp/trusted.txt")
print("\n" + "NOW, let's look inside...")
print("ropen_tester.func_closure: " + str(ropen_tester.func_closure))

if ropen_tester.func_closure is not None:
    for obj in ropen_tester.func_closure:
        print(" "*2+str(obj)+".cell_contents: " + str(obj.cell_contents))
        print(" "*2+"id("+str(obj)+".cell_contents): " + str(id(obj.cell_contents)))

#compare with __builtins__.open
print("\n" + "__builtins__.open: " + str(__builtins__.open))
print("id(__builtins__.open): " + str(id(__builtins__.open)))

print("\n" + "ropen_tester.func_code: " + str(ropen_tester.func_code))


##########

untrusted_module = __import__("nametest_notrust", globals(), {"__nametoken__": untrusted_token})

untrusted_module.getsecrets()

ropen = restricted_open(open, "/tmp")
#print("changetoken=" + str(changetoken(ropen, untrusted_token)))
untrusted_module.filewrite(ropen)
