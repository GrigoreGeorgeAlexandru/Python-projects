f=open("ex8.txt")
s=f.read()
i=0
v="AEIOUaeiou"
while i<len(s):
    if s[i] in v:
        s=s[:i+1]+'p'+s[i].lower()+s[i+1:]
        i=i+2
    i+=1
print(s)