import string

f=open("ex 11.txt")
exclude=set(string.punctuation)
lista=list()
for i in f:
    til=i.count('~')
    #print(til)
    for ch in i:
        if ch in exclude:
            i=i.replace(ch,' ')
    i=i.split()
    word=i.count(i[0])-1
    #print(word)
    lista.append((i[0],til+word))
    print(lista)
