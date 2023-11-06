import csv
import matplotlib as plt
import numpy as np
###el formato de fecha es mes-dia
def meteocat():
    data_estacions = np.genfromtxt('IV/2020_MeteoCat_Estacions.csv', delimiter=';', skip_header=1, encoding='utf-8')
    data_estacions_detall = np.genfromtxt('IV/2022_MeteoCat_Detall_Estacions.csv', delimiter=';', skip_header=1, encoding='utf-8')
    data_metadades = np.genfromtxt('IV/MeteoCat_Metadades.csv', delimiter=';', skip_header=1, encoding='utf-8')

    # print(data_estacions)
    

meteocat()
