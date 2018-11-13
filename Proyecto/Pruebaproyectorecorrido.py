A1 = [[3,5,7],[2,8,4],[5,7,4]]
A2 = [[3,5,7],[2,8,4],[5,7,4]]
AR = []
R = 0

fila = 0
f = 0

for z in range(3):
    AR.append([])
    for i in range(3):
        for j in range(3):
            R += (A1[fila][j]*A2[j][i])
            print (A1[fila][j])
            print (A2[j][i])
        print ("-------------")
        AR[f].append(R)
        R = 0
    fila += 1
    f += 1

print(R)