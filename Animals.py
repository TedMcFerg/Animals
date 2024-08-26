class Animal:
    def __init__(self, age, condition, weight):
        self.age = age
        self.health = condition
        self.weight = weight

    def eat(self):
        self.weight += 1
        farm.food -= 1
        print(f"{self.__class__.__name__} is eating.")

    def grow(self):
        self.age += 1
        if random.random() < 0.1:
            self.health -= 5
        print(f"{self.__class__.__name__} is now {self.age} days old.")

    def check_health(self):
        if self.health <= 0:
            print(f"{self.__class__.__name__} has died.")
            farm.remove_animal(self)

class Cow(Animal):
    def __init__(self, age, condition, weight):
        super().__init__(age, condition, weight)

    def moo(self):
        print("Moo!")

class Chicken(Animal):
    def __init__(self, age, condition, weight):
        super().__init__(age, condition, weight)

    def cluck(self):
        print("Cluck!")
