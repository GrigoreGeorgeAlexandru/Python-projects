f=open("ex 10.txt")

D={}

for line in f:
    line=line.split()
    D[line[0]]=set(line[1:])

inter=D[list(D.keys())[0]]
reun=D[list(D.keys())[0]]

for i in D:
    inter=inter&D[i]
    reun=reun|D[i]
    dif = D[i]
    for j in D:
        if i!=j:
            dif=dif-D[j]
    print(dif)



print(inter)
print(reun)