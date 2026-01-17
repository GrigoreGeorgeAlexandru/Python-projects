s=input()
d={}
s=s.split()
for c in s:
    d.setdefault(c,0)
    d[c]+=1


d2={}
for c in d:

    d2.setdefault(d[c], []).append(c)



k=sorted(d2)

d2[k[0]].sort()
print(d2[k[0]][0])
d2[k[-1]].sort()
print(d2[k[-1]][0])