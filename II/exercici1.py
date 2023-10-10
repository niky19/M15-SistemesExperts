#ETL from csv
import csv

def csvReader():
    data = csv.reader(open('II/basket_players.csv', 'r'))
    header = next(data)

    translation_dict = {
    'Name': 'Nom',
    'Team': 'Equip',
    'Position': 'Posició',
    'Height': 'Alçada',
    'Weight': 'Pes',    
    'Age': 'Edat'
    }   
    
    translated_header = [translation_dict.get(column.strip(), column) for column in header]

    
    print('; '.join(translated_header.values()))

    """for i, valor in enumerate(data):
        print(i, valor)
    print("Files totals: ", i)"""

csvReader()