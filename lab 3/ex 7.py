d1={"a":1,"b":2,"c":2}
d2={"c":1,"d":4,"e":5}

for k in d2:
    if k in d1:
        d1[k]+=d2[k]
    else:
        d1[k]=d2[k]
print(d1)