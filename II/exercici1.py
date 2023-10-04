#ETL from csv
import csv

def csvReader():
    data = csv.reader(open('II/basket_players.csv', 'r'))
    header = next(data)
    mydict = {columna: [] for columna in header}

    for i, valor in enumerate(data):
        print(i, valor)
    print("Files totals: ", i)

    for fila in data:
        for i, valor in enumerate(fila):
            columna = header[i]
            mydict[columna].append(valor) 
    print(mydict.keys())
csvReader()
aa