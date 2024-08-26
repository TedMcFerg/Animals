from Model_Classes import Animals

class Farm:
    def __init__(self):
        self.food = 100
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def simulate_day(self):
        for animal in self.animals:
            animal.grow()
            if self.food > 0:
                animal.eat()
            else:
                print(f"Not enough food for {animal.__class__.__name__}!")
                animal.health -= 10
            animal.check_health()
