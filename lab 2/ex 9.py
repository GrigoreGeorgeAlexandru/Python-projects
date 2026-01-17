f=open("ex9.txt")
s=f.read()

i=s.find('$')
nr1=i
while s[i+1].isdigit()==True:
    i+=1

nr2=i
n1=int(s[nr1+1:nr2+1])
i=s.find('$',nr2)
nr1=i
while s[i+1].isnumeric()==True:
    i+=1

nr2=i
n2=int(s[nr1+1:nr2+1])
print(n1)
print(n2)