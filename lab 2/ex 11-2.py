f=open("ex11.txt")
s=f.read()
s2=[]
i=s.find('.')
b=0
while i!=-1:
    if i+1==len(s) or s[i+2].isupper()==True:
        s2.append(s[b:i])
        b=i+2
        i=s.find('.',b+1)
    else:
        i = s.find('.', i + 1)
print(s2)
