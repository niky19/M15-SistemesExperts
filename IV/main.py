import csv
import numpy as np

def meteocat():
    data_estacions = csv.reader(open('IV/2020_MeteoCat_Estacions.csv', 'r'), delimiter=';')
    data_estacions_detall = csv.reader(open('IV/2022_MeteoCat_Detall_Estacions.csv', 'r'), delimiter=';')
    data_metadades = csv.reader(open('IV/MeteoCat_Metadades.csv', 'r'), delimiter=';')

    dim0 = np.array([[data_estacions, data_estacions_detall],[data_metadades]])
    print(dim0)

meteocat()
