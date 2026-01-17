f=open("graf_in.txt")
orie=f.readline()
n=int(f.readline())
nr=int(f.readline())
l=[]
for i in range(nr):
    x=f.readline()
    x=x.split()
    l.append((int(x[0]),int(x[1])))
    if orie.strip()=='neorientat':
        l.append((int(x[1]),int(x[0])))
s=f.readline()
s=s.split()
f.close()
print(l)
d={}
for i in l:
    d.setdefault(i[0],[])
    d[i[0]].append(i[1])

print(d)

m=[[0 for i in range(0,n+1,1)]for i in range(0,n+1,1)]
for i in l:
    m[i[0]][i[1]]=1
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(m[i][j],end=" ")
    print()

BF=[]
BF.append((int(s[0]),-1))
st=dr=0
while st<=dr:
    tata=BF[st][0]
    for fiul in d[tata]:
        if fiul not in [nod for (nod,parinte) in BF]:
            BF.append((fiul,tata))
            dr+=1
    st+=1

for i in BF:
    print(i[0],end=" ")
DF=[]
vizitat=[]
DF.append(int(s[0]))
vizitat.append(int(s[0]))
while DF !=[]:
    flag=0
    tata=DF[-1]
    for fiul in d[tata]:
        if fiul not in vizitat:
            flag=1
            break
    if flag==1:
        DF.append(fiul)
        vizitat.append(fiul)
    else:
        DF.pop(-1)
print()
print(vizitat)

c=int(s[1])
fl=[]
fl.append(c)
while c!=int(s[0]):
    for (fiu,tata) in BF:
        if c==fiu:
            c=tata
            fl.append(c)

            print(fl[::-1])