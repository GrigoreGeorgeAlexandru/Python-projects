v=[0]*100
def citire():
    n=input()

    for i in range(int(n)):
        global v
        v[i]=input()

def afisare():
    global v
    for i in v:
        print(i,end=" ")
    print('\n')
def valpoz():
    global v
    global list
    list=[i for i in v if int(i)>0]
def semn():
    global v
    v=[-int(i) for i in v]
