name=input()
f=open(name).read().split()
for i in range(len(f)):
    for j in range(i+1,len(f),1):
        if f[i][-1]==f[j][-1]:
            print(f[i]+' '+f[j])

