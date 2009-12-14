myname = __name__ + " (nametest.py)"
print("\n"*2 + myname + "\n" + "="*len(myname))

_nametest_secret = "The Magic Words are Squeamish Ossifrage."

import nametest_trust

myname = __name__ + " (nametest.py)"
print("\n"*2 + myname + "\n" + "="*len(myname))

filenames = ["/tmp/trusted.txt", "/tmp/notrust.txt"]
for name in filenames:
    f = open(name, "r")
    print(name + ": " + f.readline().strip())
    f.close()