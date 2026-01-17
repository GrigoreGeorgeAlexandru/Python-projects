def generator1(x):
    for i in range(2,x+1,1):
        flag=1
        for j in range(2,i//2+1,1):
            if i%j==0:
                flag=0
                break
        if flag==1:
             yield (i)

def generator2(x):
    i=1
    nr=2
    while i<=x:
        flag=1
        for j in range(2,nr//2+1,1):
            if nr%j==0:
                flag=0
                break
        if flag==1:
            yield (nr)
            i+=1
        nr+=1
f=input()

for x in generator1(int(f)):
    print(x)
print()
for x in generator2(int(f)):
    print(x)