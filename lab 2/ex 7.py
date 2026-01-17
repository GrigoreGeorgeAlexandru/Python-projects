file=open("ex7.txt")
date=file.read()
date=date.split()
D={0:"duminica",1:"luni",2:"marti",3:"miercuri",4:"joi",5:"vineri",6:"sambata"}
L={"ianuare":1,"februarie":2,"martie":3,"aprilie":4,"mai":5,"iunie":6,"iulie":7,"august":8,"septembrie":9,"octombrie":10,"noiembrie":11,"decembrie":12}
c=0
l1=[1,3,5,7,8,10,12]
l2=[4,6,9,11]

for i in range(1702,int(date[2])):
    if i%4!=0:
        c+=1
    elif i%100:
        c+=2
    elif i%400:
        c+=1
    else:
        c+=2



if date[1].isalpha():
    date[1]=L[date[1]]

for i in range(1,int(date[1]),1):
    if i in l1:
        c+=3
    elif i in l2:
        c+=2
    else:
        c+=0


if int(date[1])>2:
    if int(date[2])%4!=0:
        c+=0
    elif int(date[2])%100:
        c+=1
    elif int(date[2])%400:
        c+=0
    else:
        c+=1
c+=(int(date[0])-1)%7
c=c%7

print(D[c])