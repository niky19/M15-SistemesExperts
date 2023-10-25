import csv
import numpy as np

def meteocat():
    data_estacions = csv.reader(open('/home/nikita.barbosa.7e5/Escriptori/DADES/niki/M15-SistemesExperts/IV/2020_MeteoCat_Estacions.csv', 'r'), delimiter=';')
    data_estacions_detall = csv.reader(open('/2022_MeteoCat_Detall_Estacions.csv', 'r'), delimiter=';')
    data_metadades = csv.reader(open('/2021_MeteoCat_Metadades.csv', 'r'), delimiter=';')

    my_array = np.array([row for row in data_estacions],[row for row in data_estacions_detall],[row for row in data_metadades])
    print(my_array)


meteocat()
