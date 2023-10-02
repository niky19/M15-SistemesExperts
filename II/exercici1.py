#ETL from csv
import csv

def csvReader():
    openMyData = open('II/basket_players.csv', 'w')
    data = csv.reader(openMyData)
    print(data)
    for i, fila in enumerate(data):
        print(i,fila)
    
    
csvReader()