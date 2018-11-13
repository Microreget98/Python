import csv
def getdata():
    A = []
    File = 'C:/Users/angel/desktop/America-CSV.csv'
    with open(File, newline = '') as file:
        lector = csv.reader(file)
        for row in lector:
            A.append(row)
    print(A)
    return A

getdata()

#File = 'C:/Users/angel/desktop/America-CSV.csv'
#csv.DictReader(File, fieldnames= '')