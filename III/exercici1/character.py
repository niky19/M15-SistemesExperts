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
        
