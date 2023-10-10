
# Al .csv, les paraules Heigth i Weigth estan mal escrits, s'haurien de canviar per Height i Weight. No ho he modificat perquè no sé si és un error o si és a propòsit.
import csv

    #1. ETL from csv
def csvTransformer():
    data = csv.reader(open('II/basket_players.csv', 'r'), delimiter=';')
    header = next(data)
    catalan_columns = dict(Name="Nom", Team="Equip", Position="Posicio",
                           Heigth="Alçada", Weigth="Pes", Age="Edat")
    catalan_positions = {
        "Point Guard": "Base",
        "Shooting Guard": "Escorta",
        "Small Forward": "Aler",
        "Power Forward": "Ala-pivot",
        "Center": "Pivot"
    }

    cms = 2.54
    kg = 0.45

    translated_csv = []
    translated_header = []
    for i in header:
        translated_header.append(catalan_columns[i])
    translated_csv.append(translated_header)
    print(translated_csv)

    for i, fila in enumerate(data):
        fila[2] = catalan_positions[fila[2]]
        fila[3] = round(float(fila[3]) * cms, 2)
        fila[4] = round(float(fila[4]) * kg, 2)
        fila[5] = round(float(fila[5]))
        translated_csv.append(fila)
    print("Files totals: ", i)
    print(translated_csv)

    with open("II/jugadors_basquet.csv", "w") as f:
        writer = csv.writer(f, delimiter="^")
        writer.writerows(translated_csv)

    for i, fila in enumerate(translated_csv):
        print(i, fila)
    print("Files totals: ", i)
    
    return translated_csv

    #2.Estadístiques
def csvStats(translated_csv):
        #2.1. Jugador amb el pes més alt
    max_weight = translated_csv[1][4]
    max_weight_name = translated_csv[1][0]
    for i in range(1, len(translated_csv)):
            if (translated_csv[i][4] > max_weight):
                max_weight = translated_csv[i][4]
                max_weight_name = translated_csv[i][0]
    print("Nom del jugador amb el pes més alt:", max_weight_name, "amb", max_weight, "kg")

        #2.1 Nom del jugador amb l'alçada més baixa
    min_height = translated_csv[1][3]
    min_height_name = translated_csv[1][0]
    for i in range(1, len(translated_csv)):
            if (translated_csv[i][3] < min_height):
                min_height = translated_csv[i][3]
                min_height_name = translated_csv[i][0]
    print("Nom del jugador amb l'alçada més baixa:", min_height_name,"amb", min_height, "cm")
    
        #2.3. Mitjana de pes i alçada de jugador per equip.

if __name__ == "__main__":
    translated_csv = csvTransformer()
    csvStats(translated_csv)


