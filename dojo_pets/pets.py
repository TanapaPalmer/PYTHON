from dojo_pets import Ninja

class Pet(Ninja):
    

    def __init__ (self, pet_name, pet_type, pet_tricks):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.pet_tricks = pet_tricks
        self.ninja = Ninja(first_name = "Sandra", last_name = "Louise", treats = "Jerky", pet_food = "Burger", pet_type = "Puppy Doggie", energy = 0, health = 0)

    def sleep(self, energy):
        print(f'{self.ninja.first_name} takes {self.pet_name} to sleep because it is a bed time!')
        if energy > 1:
            self.ninja.bathe(energy)
            print(f'Now {self.pet_name} has {self.ninja.energy} energy and {self.ninja.health} health.')
        return self

    def eat(self, energy, health):
        print(f'{self.ninja.first_name} feeds {self.pet_name}!')
        if energy > 1:
            self.ninja.feed(energy, health)
            print(f'{self.pet_name} had some {self.ninja.pet_food}.')
            print(f'Now {self.pet_name} has {self.ninja.energy} energy and {self.ninja.health} health!')  
        return self

    def get_snack(self, energy, health):
        print(f'{self.ninja.first_name} gives some snack to {self.pet_name}!')
        if energy > 1:
            print(f'{self.pet_name} had some {self.ninja.treats}.')
            self.ninja.feed(energy, health)
            print(f'Now {self.pet_name} has {self.ninja.energy} energy and {self.ninja.health} health!')
        return self


    def play(self, health):
        print(f'{self.ninja.first_name} takes {self.pet_name} for a walk!')
        if health > 1:
            self.ninja.walk(health)
            print(f'Now {self.pet_name} has {self.ninja.health} health.')
        return self


    def noise(self):
        print(self.ninja.first_name, "cleans", self.pet_name)
        print("Looks clean now!")
        if self.ninja.pet_type == "Puppy Doggie":
            print("Yip Yip!")
        elif self.ninja.pet_type == "Kitten":
            print("Meow Meow!")
        return self


    def sum_score(self):
        if self.ninja.energy < 10:
            print("Oh no! Let's feed your pet!")
        elif self.ninja.health < 10:
            print("Oh no! Let's play with your pet!")
        else:
            print("Looks like your pet has a lot of energy and health. Congratulations! Your pet is very healthy!")
        return self
        

sandra = Pet ("BooBoo", "Dachshund", "Hi5")


sandra.play(5)
sandra.eat(5, 10)
sandra.get_snack(5, 10)
sandra.noise()
sandra.sleep(25)
sandra.sum_score()


