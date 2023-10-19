import json
from types import SimpleNamespace
from character import Character
def playingWithJson():
    with open('/home/nikita.barbosa.7e5/Escriptori/DADES/niky/M15-SistemesExperts/III/exercici1/StarWars.json', 'r') as starwars:
        file_contents = starwars.read()
        
        my_data_dic =  json.loads(file_contents)
        print(type(my_data_dic))

    
        character_film_list = []
        for i in my_data_dic:
                character_film_list.append(i)
        
        print(character_film_list)
        print(type(character_film_list))

playingWithJson()
