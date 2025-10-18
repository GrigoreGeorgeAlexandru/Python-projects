#autor:Grigore George Alexandru grupa 232

states=[]                           #definim listele goale in care vom stoca starile,literele,tranzitiile
letters = []                                    # starea de inceupt si starile finale
start=[]
final=[]
flag=0
Tstates=[]
Tstates2=[]
Tletters=[]
with open("input.in") as f:
    for line in f:                  #parcurgem fisierul linie cu linie
        if line.startswith('#'):
            continue                #sarim peste comentarii
        if "Sigma" in line:         #intram in sectiunea sigma a fisierului
            for line in f:
                if "End" in line:   #cand ajungem la la finalul segmentului iesim din for-ul curent
                    break
                else:
                    letters.append(line.strip())   #adaugam fiecare litera in lista

        if "States" in line:         #intram in sectiunea states a fisierului
            for line in f:
                if "End" in line:   #cand ajungem la la finalul segmentului iesim din for-ul curent
                    break
                else:
                    curent=[x.strip() for x in line.split(',')]  #luam fiecare linie si verificam daca contine mai mult
                    if len(curent)==1:                           #decat numele starii
                        states.append(curent[0])
                    elif curent[1]=='S':                         # daca linia contine 'S' adaugam starea ca stare de start
                        start.append(curent[0])
                        states.append(curent[0])
                    else:
                        final.append(curent[0])                  #altfel o adaugam ca stare de final
                        states.append(curent[0])
        if(len(start)>1):                                        #daca avem mai multe stari initiale inputul este invalid si terminam programul
            print("invalid")
            flag=1
            break
        if "Transitions" in line:   #intram in sectiunea de tranzitii din document
            for line in f:
                if "End" in line:   #cand ajungem la la finalul segmentului iesim din for-ul curent
                    break
                curent = [x.strip() for x in line.split(',')]
                Tstates.append(curent[0])                       #stocam valorile din fiecare tranzitie
                Tstates2.append(curent[2])
                Tletters.append(curent[1])

for element in Tstates:                 #verificam daca fiecare stare din tranzitii este valida
    if element not in states:
        print("invalid")            #daca nu este inputul este invalid si terminam programul
        flag=1
        break

for element in Tstates2:                 #verificam daca fiecare stare din tranzitii este valida
    if element not in states:
        print("invalid")            #daca nu este inputul este invalid si terminam programul
        flag=1
        break

for element in Tletters:            #verificam daca fiecare litera  din tranzitii este valida
    if element not in letters:
        print("invalid")
        flag=1                      #daca nu este inputul este invalid si terminam programul
        break
if(flag==0):                      #daca flagul nu a fost ridicat pana acum inseamna ca programul e valid
    print("valid")
