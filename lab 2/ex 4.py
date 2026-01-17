c1=input("c1:")
c2=input("c2:")

flag=1

if len(c1)==len(c2):
    for i in range(len(c1)):
        a=c1[i]
        if c2.find(a)>=0:
            c2=c2.replace(a, '', 1)
        else:
            flag=0
            break
else:
    flag=0
if flag==1:
    print("DA")
else:
    print("NU")
