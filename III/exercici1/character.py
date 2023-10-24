class Character:
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year) -> None:
        self.edited = edited
        self.name = name
        self.created = created
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birth_year

    @property
    def info(self, name, gender, homeworld, birth_year):
            return self.name, self.gender, self.homeworld, self.birth_year
        
        ##para que sea un diccionario y que se pueda guardar en un json
    def to_dict(self):
        return {
            'edited': self.edited,
            'name': self.name,
            'created': self.created,
            'gender': self.gender,
            'skin_color': self.skin_color,
            'hair_color': self.hair_color,
            'height': self.height,
            'eye_color': self.eye_color,
            'mass': self.mass,
            'homeworld': self.homeworld,
            'birth_year': self.birth_year
        }
