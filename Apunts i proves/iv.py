import numpy as np

# Lee el archivo y guarda las líneas
with open('Apunts i proves/2020_MeteoCat_Estacions.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Extrae los encabezados y los datos
headers = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]

# Convierte la lista de datos a un array NumPy
data_array = np.array(data)

# Muestra los encabezados y los primeros cinco datos
print("Encabezados:", headers)
print("Datos:")
print(data_array[:5])  # Muestra los primeros cinco datos para visualización
