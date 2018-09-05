def Binaria():
    x = []
    n = 3
    cont = 0
    p = pow(2,n) 
    print (str(p) + " esto es p")
    j = 2
    d = 1
    b1 = 0
    b2 = 1
    sw = 0
    for a in range(n):
        x.append([])
        for b in range(int(p)):
            if sw == 0:
                while cont < d:
                    x[a].append(0)
                    cont = cont + 1
                    print (x[a])
                    sw = 1
                cont = 0
            elif sw == 1:
                while cont < d:
                    x[a].append(1)
                    cont = cont + 1
                    print (x[a])
                    sw = 0
                cont = 0          
        p = p / 2
        print (str(p) + " esto es p en for")
        j = j - 1
        cont = 0
        d = d * 2
    

Binaria()