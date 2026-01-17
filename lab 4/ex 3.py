import sys
def min_max(*nrs):
    mini=None
    maxi=None
    for nr in nrs:
        if mini==None or mini>nr:
            mini=nr
        if maxi==None or maxi<nr:
            maxi=nr
    if mini!=None and maxi!=None:
        return mini,maxi
    else:
        return None

try:
    file=open("numere.txt")
except OSError:
    print("creati fisierul de intrare")
    sys.exit()
nrs=file.read()
nrs=nrs.split()
try:
    nrs=[int(i) for i in nrs]
except ValueError:
    print("fisierul contine un non-numar")
    sys.exit()
p=min_max(*nrs)

g=open("impartire.txt","w")
try:
    g.write(str(p[1]/p[0]))
except ZeroDivisionError:
    print("nu se poate imparti la zero")
    sys.exit()
except IOError:
    print("make the file writable")
    sys.exit()