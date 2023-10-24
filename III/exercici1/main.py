import json
from types import SimpleNamespace
from character import Character

def playingWithJson():
    extra_info_names = ["Luke Skywalker", "Chewbacca", "Anakin Skywalker"]
    with open('III/exercici1/StarWars.json', 'r') as file:
        data = json.load(file)
        
        character_film_list = []
        for i in data:
            character_film_list.append(Character(**i['fields']))
        

        for i in character_film_list:
            if i.name == extra_info_names[0]:
                i.num_of_films = 6
                i.first_film = "A New Hope"
                i.alive_at_the_end = False
            if i.name == extra_info_names[1]:
                i.num_of_films = 5
                i.first_film = "A New Hope"
                i.alive_at_the_end = True
            if i.name == extra_info_names[2]:
                i.num_of_films = 3
                i.first_film = "The Phantom Menace"
                i.alive_at_the_end = False

    with open('III\exercici1\character_film_list.json', 'w') as f:
        json.dump(character_film_list, f, default=lambda o: o.__dict__)

playingWithJson()