import csv
import numpy as np
import matplotlib.pyplot as plt

def meteocat():
    with open('IV/2020_MeteoCat_Estacions.csv', 'r', encoding='utf-8') as f:
        estacions = np.array(list(csv.reader(f, delimiter=';')))

    with open('IV/2022_MeteoCat_Detall_Estacions.csv', 'r', encoding='utf-8') as f:
        estacions_detall = np.array(list(csv.reader(f, delimiter=';')))

    with open('IV/MeteoCat_Metadades.csv', 'r',encoding='utf-8') as f:
        metadades = np.array(list(csv.reader(f, delimiter=';')))

    print(estacions.shape)
    print(estacions_detall.shape)
    print(metadades.shape)

    

    





"""nom_estacio = [fila[0] for fila in data_estacions] 
    valor = [fila[1] for fila in data_estacions_detall] 
    for i, nombre in enumerate(nom_estacio):
        plt.plot(valor[i], label=nombre)

    plt.xlabel('Fecha')
    plt.ylabel('Temperatura media (°C)')
    plt.title('Comparativa de la temperatura media diaria en febrero de 2022')
    plt.legend()
    plt.show()"""

meteocat()
