f=open("ex6.txt")
s=f.read()
s=s.split()
d={}
for c in s:
    c=list(c)
    for i in c:
        d.setdefault(i,0)
        d[i]+=1
print(d)
