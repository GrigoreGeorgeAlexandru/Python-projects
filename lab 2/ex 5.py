c=input("c:")
c2=[None]*len(c)
k=int(input('k:'))
for i in range(len(c)):
    if 'A'<=c[i]<='Z' and chr(ord(c[i]) + k)>'Z':
        c2[i]=chr(ord(c[i]) + k-26)
    elif chr(ord(c[i]) + k)>'z':
        c2[i]=chr(ord(c[i]) + k-26)
    else:
        c2[i]=chr(ord(c[i]) + k)

print(c2)
