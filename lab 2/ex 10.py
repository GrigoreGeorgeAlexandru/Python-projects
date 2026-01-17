f=open("ex10.txt")
s=f.read()
s=s.split()
f=1
for i in range(len(s)):
    if i>=2:
        print(1)
        f=0
        break
    if s[i][0].islower():
        print(2)
        f=0
        break
    if len(s[i])<3:
        print(3)
        f=0
        break

    if s[i].count('-')>=2 :
        print(4)
        f=0
        break
    for j in range(len(s[i])):
        if s[i][j].isalpha()==False and s[i][j]==False:
            print(5)
            f=0
            break
    if f==0:
        break

if(f==1):
    print("DA")
else:
    print("NU")

