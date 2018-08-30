def Binaria():
    x = []
    n = 3
    cont = 0
    for i in range(n):
        x.append(0)
    p = pow(2,n) 
    print (str(p) + " esto es p")
    j = 2
    d = 1
    sw = 0
    for i in range(n):
        for i in range(int(p)):
            if sw == 0:
                while cont < d:
                    x[j] = 0
                    cont = cont + 1
                    print (x[j])
                    sw = 1
                cont = 0
            elif sw == 1:
                while cont < d:
                    x[j] = 1
                    cont = cont + 1
                    print (x[j])
                    sw = 0
                cont = 0          
        p = p / 2
        print (str(p) + " esto es p en for")
        j = j - 1
        cont = 0
        d = d * 2
    

Binaria()