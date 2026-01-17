f=open("ex8-4.txt")
s=f.read()
i=0
v=" -."
while i<len(s):
    if s[i] in v:
        s=s[:i]+'p'+s[i-1].lower()+s[i:]
        i=i+2
    i+=1
print(s)