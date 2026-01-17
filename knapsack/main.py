import itertools


f = open("input.in", "r")
k = int(f.readline())
v = list(map(int, (f.read().strip().split())))
lista = list()
for i in range(len(v)):
    for s in itertools.combinations(v,i):
     lista.append(sum(s))
maxi=0
for i in range(len(lista)):
    if maxi<lista[i]<=20 :
        maxi=lista[i]
print(maxi)