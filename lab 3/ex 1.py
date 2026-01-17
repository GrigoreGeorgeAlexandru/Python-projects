from string import digits, ascii_lowercase, ascii_uppercase
from random import choices

f=open("ex1in.txt")
g=open("ex1out.txt","w")

for line in f:
    line=line.lower()
    line=line.split()
    email=line[1]+"."+line[0]+"@myfmi.unibuc.ro"
    A = choices(ascii_uppercase)
    a = choices(ascii_lowercase, k=3)
    cif = choices(digits, k=4)
    parola = "".join(A + a + cif)
    g.write(email + "," + parola + "\n")