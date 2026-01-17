def poz_neg(*list):
    p=[i for i in list if int(i)>0]
    n=[i for i in list if int(i)<0]
    return p,n

x=input()
f=open(x,"r+")
list=f.read()
list=list.split()
list=[int(i) for i in list]

list=poz_neg(*list)
list[0].sort()
list[1].sort()
f.write(str(list[0]))
f.write('\n')
f.write(str(list[1]))
f.write('\n')