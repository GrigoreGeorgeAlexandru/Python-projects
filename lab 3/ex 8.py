cuv=input()
f=open("ex 8.txt")
d={',','.','-'}
line=f.readline()
for i in d:
    line=line.replace(i,'')
#print(line)
line=line.split()

for w in line:
    flag=1
    for i in cuv:
        if i not in w:
            flag=0
            break
    if flag==1:
        print(w)


