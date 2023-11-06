import csv
import matplotlib as plt
import numpy as np
###el formato de fecha es mes-dia
def meteocat():
    data_estacions = np.genfromtxt('IV/2020_MeteoCat_Estacions.csv', delimiter=';', skip_header=1, encoding='utf-8')
    data_estacions_detall = np.genfromtxt('IV/2022_MeteoCat_Detall_Estacions.csv', delimiter=';', skip_header=1, encoding='utf-8')
    data_metadades = np.genfromtxt('IV/MeteoCat_Metadades.csv', delimiter=';', skip_header=1, encoding='utf-8')

    """
    print("Datos de estaciones:")
    print(data_estacions[:5])  # Muestra las primeras 5 filas
    print("Datos detallados de estaciones:")    
    print(data_estacions_detall[:5])  # Muestra las primeras 5 filas
    print("Metadatos:")
    print(data_metadades[:5])  # Muestra las primeras 5 filas
    """
    # Suponiendo que 'data_estacions' contiene los datos del archivo CSV

    # Encuentra la fila que tiene el código de estación "C5"
    codigo_estacion = "C5"
    fila_estacion = data_estacions[data_estacions[:, 0] == codigo_estacion]

    # Obtén el nombre de la estación si se encuentra el código
    if fila_estacion.size > 0:
        nombre_estacion = fila_estacion[0, 1]  # El nombre de la estación está en la segunda columna (índice 1)
        print(f"El nombre de la estación con el código {codigo_estacion} es: {nombre_estacion}")
    else:
        print(f"No se encontró la estación con el código {codigo_estacion}")

meteocat()
