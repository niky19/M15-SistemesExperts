#ETL from csv
import csv

def csvReader():
    data = csv.reader(open('II/basket_players.csv', 'r'))
    for i, fila in enumerate(data):
        print(i,fila)
    
csvReader()