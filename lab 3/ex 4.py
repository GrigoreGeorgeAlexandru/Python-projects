s=input()
s=s.split()
s.sort()
nr1=s[-1]
nr2=0
flag=0
if s[0]!=s[-1]:
    flag=1
    for i in range(len(s)-1,-1,-1):
        if s[i]!=nr1:
            nr2=s[i]
            break
else:
    print("Nu exista")
if flag==1:
    print(str(nr1)+" "+str(nr2))