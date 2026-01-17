t=input()
l=list()
i=1
D={}
while t != "-1":
    t=t.split()
    l.append((t[0],t[1],i))
    D.setdefault(t[0],[])
    D[t[0]].append((t[1],i))
    i+=1
    t=input()
print(l)
s=set(ch[0] for ch in l)
print(s)
print(D)