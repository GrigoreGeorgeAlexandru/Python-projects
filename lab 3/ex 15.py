f=open("persoane.in")
punct={':',',','{','}'}
d={}
d2={}
for line in f:
    for i in punct:
        line=line.replace(i,' ')
    line=line.split()
    print(line)

    d.setdefault("nume",[])
    d["nume"].append(line[line.index("nume")+1])
    d.setdefault("prenume", [])
    d["prenume"].append(line[line.index("prenume") + 1])
    d.setdefault("adresa",{})
    d["adresa"].setdefault("oras",[])
    d["adresa"].setdefault("strada", [])
    d["adresa"].setdefault("numar", [])
    d["adresa"]["oras"].append(line[line.index("oras")+1])
    d["adresa"]["strada"].append(line[line.index("strada") + 1])
    d["adresa"]["numar"].append(line[line.index("numar") + 1])
    d2.setdefault(line[line.index("oras")+1],[])
    d2[line[line.index("oras")+1]].append(line[line.index("nume")+1]+" "+line[line.index("prenume") + 1])
print(d)
print(d2)