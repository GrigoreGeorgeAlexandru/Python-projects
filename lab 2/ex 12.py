f=open("ex12.txt")
s1=f.readline()
s2=f.readline()
s1=s1.strip()
while s1[-1]==s2[0]:
    nr=s2[0]
    while nr==s1[-1]:
        s1=s1[:-1]
    while nr==s2[0]:
        s2=s2[1:]



print(s1+s2)