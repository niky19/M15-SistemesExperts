import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#3. Temperatura mitjana de febrer

df_estacions = pd.read_csv('IV/2020_MeteoCat_Estacions.csv', delimiter=',', encoding='utf-8')
df_estacions.columns = df_estacions.columns.str.strip()
print(df_estacions.columns)
df = pd.read_csv('IV/2022_MeteoCat_Detall_Estacions.csv', delimiter=',', encoding='utf-8')
df.columns = df.columns.str.strip()
#print(df.columns)


df['DATA_LECTURA'] = pd.to_datetime(df['DATA_LECTURA'])
#Aqui cogemos los datos que nos interesan (fecha, valor y acronimo)
df_feb = df[(df['DATA_LECTURA'] >= '2022-02-01') & (df['DATA_LECTURA'] < '2022-03-01') & (df['ACRÒNIM'] == 'TM')]
#print(df_feb)

#Aqui se calcula la mediana con la funcion mean(), apartir del VALOR
df_feb_grouped = df_feb.groupby(['CODI_ESTACIO', 'DATA_LECTURA','ACRÒNIM'])['VALOR'].mean().round(1).reset_index()
df_feb_grouped_estacions = df_feb_grouped.merge(df_estacions[['CODI_ESTACIO', 'NOM_ESTACIO']], on='CODI_ESTACIO', how='left')
print(df_feb_grouped_estacions)


plt.style.use("Solarize_Light2")

fig, ax = plt.subplots()


for estacion in df_feb_grouped_estacions['NOM_ESTACIO'].unique():
    df_estacion = df_feb_grouped_estacions[df_feb_grouped_estacions['NOM_ESTACIO'] == estacion]
    ax.bar(df_estacion['DATA_LECTURA'], df_estacion['VALOR'], label=estacion)#esto es lo que crea mi grafico

ax.legend()
ax.set_xlabel('Data')
ax.set_ylabel('Temperatura mitja diaria')
ax.set_title('Temperatura mitjana de Febrer 2022')
plt.show()



#4. Predicció temperatura mes de Febrer
