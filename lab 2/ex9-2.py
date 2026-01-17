f=open("ex9-2.txt")
s=f.read()

for i in range(len(s)-1,-1,-1):
    if s[i]=='$':
        break
nr1=i
print(s[nr1])
while s[i+1].isdigit()==True:
    i+=1

nr2=i
print(s[nr2+1])
n1=int(s[nr1+1:nr2+1])
for i in range(nr1-1,-1,-1):
    if s[i]=='$':
        break
nr1=i
print(s[nr1])
while s[i+1].isdigit()==True:
    i+=1

nr2=i
print(s[nr2+1])
n2=int(s[nr1+1:nr2+1])
print(n1)
print(n2)