import matplotlib.pyplot as plt

# Datos de ejemplo (X e Y)
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

# Crear el gráfico
plt.figure(figsize=(8, 6))  # Tamaño del gráfico (opcional)

# Graficar X vs Y
plt.plot(X, Y, marker='o', linestyle='-')

# Etiquetas de los ejes y título del gráfico
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de X e Y')

# Mostrar la cuadrícula (opcional)
plt.grid(True)

# Mostrar el gráfico
plt.show()
