

class Graph:  # graful problemei
    def __init__(self, ardere, dimensiuni, harta, oameni):
        self.ardere = ardere
        self.dimensiuni = dimensiuni
        self.harta = harta
        self.oameni = oameni
    def genereazaVecini (self,nodCurent,om):
        vecini=[]
        if om[0]-1>=0:
            vecini.append([nodCurent.harta[om[0]-1][om[1]],om[0]-1,om[1]])
        if om[0] + 1 < nodCurent.dimensiuni[0]:
            vecini.append([nodCurent.harta[om[0]+1][om[1]],om[0]+1,om[1]])
        if om[1] - 1 >= 0:
            vecini.append([nodCurent.harta[om[0]][om[1]-1],om[0],om[1]-1])
        if om[1] + 1 <  nodCurent.dimensiuni[1]:
            vecini.append([nodCurent.harta[om[0]][om[1]+1],om[0],om[1]+1])
        return vecini
    def genereazaSuccesori(self, nodCurent):
        listaSuccesori=[nodCurent.harta]
        for om in oameni:
            for hartacurenta in listaSuccesori:
                for vecin in self.genereazaVecini(nodCurent,om):
                    if vecin[0]=='#':
                        hartacurenta[vecin[1]][vecin[2]]='.'
                    if vecin[0]=='~':
                        om[0]=vecin[1]
                        om[1]=vecin[2]
                    if















#D:\Gaming\games\python\tema1ia\input\input.txt

#pathi = input("input:")  #primirea caii pt fisierul de intrare
#fi=open(pathi)

fi=open("D:\\Gaming\\games\\python\\tema1ia\\input\\input.txt")
#print(f.readline())

#D:\Gaming\games\python\tema1ia\output

#patho = input("output:")                 #primirea caii pt fisierere de iesire
#fo = open(patho+"\\output.txt", "w")
fo = open("D:\\Gaming\\games\\python\\tema1ia\\output"+"\\output.txt", "w")

#nsol=input("nsol=")
nsol=1
#timeout=input("time=")
timeout=1

#citirea datelor din fisier
ardere={}
harta=[]
x=0
y=0
pompieri=[]
for line in fi:                   #citim datele de intrare
    if line !="harta\n":
      ardere[line[0]]=line.strip()[-1]
    else: break
for line in fi:
    if '@' in line:
        pompieri.append((line.index('@')))
    if line != "oameni\n":
        y=y+1
        x= len(line.strip())
    if line != "oameni\n":
      harta.append(line.strip())
    else:
        break
oameni=[]
dimensiuni=[x,y]
for line in fi:
    oameni.append((line[0],line.strip()[-1]))
print(oameni)



gr=Graph(ardere,dimensiun,harta,oameni)