import json
from types import SimpleNamespace
from character import Character

def playingWithJson():
    extra_info = {
        "Luke Skywalker": {"num_of_films": 6, "first_film": "A New Hope", "alive_at_the_end": False},
        "Chewbacca": {"num_of_films": 5, "first_film": "A New Hope", "alive_at_the_end": True},
        "Anakin Skywalker": {"num_of_films": 3, "first_film": "The Phantom Menace", "alive_at_the_end": False}
    }

    with open('III/exercici1/StarWars.json', 'r') as file:
        data = json.load(file)
        
        character_film_list = []
        for i in data:
            character = Character(**i['fields'])
            if character.name in extra_info:
                character.__dict__.update(extra_info[character.name])
            character_film_list.append(character)

    with open('III\exercici1\character_film_list.json', 'w') as f:
        json.dump(character_film_list, f, default=lambda o: o.__dict__)

playingWithJson()
