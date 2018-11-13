from Inserciondatos import getdata

path = 'C:/Users/angel/desktop/America-CSV.csv'

class Equipo():
    def prop():
        nombre = ""
        TMW = ""
        TML = ""
        TMD = ""
        Average = ""

    def data():
        T = []
        R = []
        D = []
        for i in A:
            for j in A:
                if i == 0 and j == 0:
                    nombre = A[i][j]
                elif (i >= 1 and j == 0):
                    T.append(A[i][j])
                elif (i == 0 and j >= 1):
                    R.append(A[i][j])
                elif (i >= 1 and j >= 1):                 
                    D.append(A[i][j])