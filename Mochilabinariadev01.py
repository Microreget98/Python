class Mochilabinaria:
    def Binaria():
        x = []
        #c = [peso,ben]
        n = 3
        cont = 0
        p = pow(2,n) 
        print (str(p) + " esto es p")
        sw = 0
        d = 1
        for a in range(n):
            x.append([])
            for b in range(int(p)):
                if sw == 0:
                    while cont < d:
                        x[a].append(0)
                        cont = cont + 1
                        sw = 1
                    cont = 0
                elif sw == 1:
                    while cont < d:
                        x[a].append(1)
                        cont = cont + 1
                        sw = 0
                    cont = 0          
            p = p / 2
            print (str(p) + " esto es p en for")
            #j = j - 1
            cont = 0
            d = d * 2
        ben = [8,5,2]
        peso = [5,7,2]
        return x, ben, peso

def main():
    pass

if __name__ == '__main__':
    main()
    Mochilabinaria.Binaria()