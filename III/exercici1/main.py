import json
from types import SimpleNamespace
from character import Character
def playingWithJson():
    with open('III/exercici1/StarWars.json', 'r') as file:
        data = json.load(file)
        print(data)
        character_film_list = list(data)
        print(character_film_list[0])



playingWithJson()
