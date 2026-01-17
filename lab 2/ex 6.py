f=open("ex 6.txt")

s=f.read()

s=s.split()
suma=0
for i in range(len(s)):
    if "RON" in s[i]:
        suma+=int(s[i-1])


print(suma)

