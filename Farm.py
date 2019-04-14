from Model_Classes import Animals

class Farm:
  def __init__(self, title, funds):
    self.name = title
    self.money = funds
    self.number_animals=0
    self.food = self.money *5
    self.animals = [Animals.Animal(10, 2, 7), Animals.Animal(1, 5, 15), Animals.Animal(5, 7, 25)]
    self.description = title + " Farm"

