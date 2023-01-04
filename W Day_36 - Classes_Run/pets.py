#1
class qpet:
    def __init__(self, name, anitype, age):
        self.name = name
        self.animalType = anitype
        self.age = age

    def set_name(self, name):
        self.name = name
    
    def set_animal_type(self, anitype):
        self.animalType = anitype
        
    def set_age(self, age):
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_animal_type(self):
        return self.animalType
    
    def get_age(self):
        return self.age
    
    def _str_(self):
        return f'Name: {self.name} \nAnime Type: {self.animalType} \nAge: { self.age}'