from Character import *

class Character_films(Character):
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year,num_of_films, first_film,alive_at_the_end) -> None:
        super().__init__(edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year)
        self.__num_of_films = num_of_films
        self.__first_film = first_film
        self.__alive_at_the_end = alive_at_the_end

    @property
    def num_of_films(self):
        return self._num_of_films
    
    @num_of_films.setter
    def num_of_films(self, new):
        self._num_of_films = new

    @num_of_films.deleter
    def num_of_films(self):
        del self.__num_of_films   