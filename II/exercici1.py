#ETL from csv
import csv

def csvReader():
    data = csv.reader(open('II/basket_players.csv', 'r'), delimiter=';')
    header = next(data)
    mydict = []

    for i in header:
        mydict.append(i)

    catalan = dict(Name="Nom",Team="Equip", Position="Posicio", Height="Alçada", Weight="Pes", Age="Edat")

    for i in range(len(mydict)):
        if mydict[i] == "Name":
            mydict[i] = catalan["Name"]
        elif mydict[i] == "Team":
            mydict[i] = catalan["Team"]
        elif mydict[i] == "Position":
            mydict[i] = catalan["Position"]
        elif mydict[i] == "Height":
            mydict[i] = catalan["Height"]
        elif mydict[i] == "Weight":
            mydict[i] = catalan["Weight"]
        elif mydict[i] == "Age":
            mydict[i] = catalan["Age"]
    print(mydict)

    for i, fila in enumerate(data):
        #print(i, fila)
        mydict.append(fila)
    print("Files totals: ", i)





    """print(mydict[0]) -> Name
    print(catalan["Name"]) -> Nom
    print(catalan[mydict[0]]) -> Nom
    """
    
    

 
csvReader()