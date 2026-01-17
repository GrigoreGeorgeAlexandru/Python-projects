f=open("ex8-2.txt")
s=f.read()
i=0
v="AEIOUaeiou"
while i<len(s):
    if s[i] in v:
        s=s[:i+1]+s[i+3:]
    i+=1
print(s)