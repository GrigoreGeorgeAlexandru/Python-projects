n=5
m=n*n
q=1
d=[[0 for i in range(n)]for j in range(n)]
print(d)
for i in range(n):
    for j in range(n):
        #print(str(i)+str(j))
        d[i][j]=q
        q+=1

print(d)
l=[]
q=0
while n-1>0:
    i=q
    j=q
    for j in range(q,n,1):
        l.append((i,j))
    for i in range(q+1,n,1):
        l.append((i,j))
    for j in range(n-2,q+-1,-1):
        l.append((i,j))
    for i in range(n-2,q+0,-1):
        l.append((i, j))
    n-=1
    q+=1
print(l)

l2=[0]*m
print(l2)
j=0

for i in l:
    l2[j]=5*i[0]+i[1]+1
    j+=1

print(l2)