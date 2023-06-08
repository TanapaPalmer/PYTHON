

class Ninja:


    def __init__ (self, first_name, last_name, treats, pet_food, pet_type, energy, health):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet_type = pet_type
        self.energy = energy
        self.health = health


    def walk(self, health):
        self.health += health
        return self


    def feed(self, energy, health):
        self.energy += energy
        self.health += health
        return self


    def bathe(self, energy):
        self.energy += energy
        return self


