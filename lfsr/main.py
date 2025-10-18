

class LFSR():


    def __init__(self, s ,c):
        self.register = s
        self.coefficients = c


    def step(self):
        #calculez bit-ul nou conform formulei din carte
        new_bit=0
        for i in range(len(self.register)):
            new_bit = self.coefficients[i]*self.register[-1-i] + new_bit
            new_bit = new_bit % 2
        #shiftez secventa si adaug bit-ul nou la final
        del self.register[0]
        self.register.append(new_bit)
        return self.register




def main():
    #citesc s-urile
    s=[int(i) for i in input("s=")]
    #citesc c-urile
    c = [int(i) for i in input("c=")]

    #creez starea initiala
    register = LFSR(s=s,c=c)
    output=[]
    #initialiez outputul
    output.append(s[0])
    print("Step 0\n{}".format(s))
    # shiftarea pentru fiecare pas
    for i in range(15):
        r = register.step()
        #adaug treptat prima valoare din fiecare pas la output
        output.append(r[0])
        print("Step {}\n{}".format(i + 1, r))
    print("output: ")
    print(output)
if __name__ == "__main__":
    main()


