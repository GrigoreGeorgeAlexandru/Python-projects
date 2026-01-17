f=open("ex8-3.txt")
s=f.read()
i=0
v="- ."
while i<len(s):
    if s[i] in v:
        s=s[:i-2]+s[i:]
    i+=1
print(s)
s=s.replace('-','')
print(s)