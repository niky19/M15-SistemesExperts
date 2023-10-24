
class Character_films(Character):
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year,num_of_films, first_film,alive_at_the_end) -> None:
        super().__init__(edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year)
        self.num_of_films = num_of_films
        self.first_film = first_film
        self.alive_at_the_end = alive_at_the_end


    @property
    def num_of_films(self):
        return self._num_of_films
    
    @num_of_films.setter
    def num_of_films(self, new):
        self._num_of_films = new

    @num_of_films.deleter
    def num_of_films(self):
        del self.__num_of_films
    
    @property
    def first_film(self):
        return self.first_film
    
    @first_film.setter
    def first_film(self, new):
        self.first_film = new

    @first_film.deleter
    def first_film(self):
        del self.first_film
    
    @property
    def alive_at_the_end(self):
        return self.alive_at_the_end
    
    @alive_at_the_end.setter
    def alive_at_the_end(self, new):
        self.alive_at_the_end = new

    @alive_at_the_end.deleter
    def alive_at_the_end(self):
        del self.alive_at_the_end