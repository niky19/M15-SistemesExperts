import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def make_a_graph(ax, df, title, xlabel, ylabel):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def make_a_histo(ax, df, title, xlabel, ylabel):
    ax.set_xlabel(xlabel)  # Restaurar las etiquetas de los ejes X e Y
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    sorted_index = df.index.sort_values()
    plt.hist(df.values, bins=10)
    plt.show()

def mean_temp():
    #3. Temperatura mitjana de febrer

    df_estacions = pd.read_csv('IV/2020_MeteoCat_Estacions.csv', delimiter=',', encoding='utf-8')
    df_estacions.columns = df_estacions.columns.str.strip()
    #print(df_estacions.columns)
    df = pd.read_csv('IV/2022_MeteoCat_Detall_Estacions.csv', delimiter=',', encoding='utf-8')
    df.columns = df.columns.str.strip()
    #print(df.columns)


    df['DATA_LECTURA'] = pd.to_datetime(df['DATA_LECTURA'])
    #Aqui cogemos los datos que nos interesan (fecha, valor y acronimo)
    df_feb = df[(df['DATA_LECTURA'] >= '2022-02-01') & (df['DATA_LECTURA'] < '2022-03-01') & (df['ACRÒNIM'] == 'TM')]


    #Aqui se calcula la mediana con la funcion mean(), apartir del VALOR
    df_feb_grouped = df_feb.groupby(['CODI_ESTACIO', 'DATA_LECTURA','ACRÒNIM'])['VALOR'].mean().round(1).reset_index()
    df_feb_grouped_estacions = df_feb_grouped.merge(df_estacions[['CODI_ESTACIO', 'NOM_ESTACIO']], on='CODI_ESTACIO', how='left')

    plt.style.use("Solarize_Light2")

    fig, ax = plt.subplots()


    for estacion in df_feb_grouped_estacions['NOM_ESTACIO'].unique():
        df_estacion = df_feb_grouped_estacions[df_feb_grouped_estacions['NOM_ESTACIO'] == estacion]
        ax.plot(df_estacion['DATA_LECTURA'], df_estacion['VALOR'], label=estacion)#esto es lo que crea mi grafico

    make_a_graph(ax, df_feb_grouped_estacions, 'Temperatura mitjana de febrer', 'DATA_LECTURA', 'VALOR')


    #4. Predicció temperatura mes de Febrer
    value_conts =df_feb_grouped_estacions['VALOR'].value_counts()
    print(value_conts)
    fig, ax = plt.subplots()
    make_a_histo(ax, value_conts, 'Predicción temperatura mes de Febrero', 'FREQ', 'VALOR')  # Restaurar etiquetas de X e Y

