# Library of classes and functions

class farm:
  def __init__(self, title, funds):
    self.name = title
    self.money = funds
    self.number_animals=0
    self.food = self.money *5
  description = "Words"

  class animal:
    def __init__(self, age, condition):
      self.age = age
      self.health = condition


    def eat():
      print("eating")

MyFarm = farm("Mine", 0)
Myanimal = MyFarm.animal(2, 50)
MyFarm.animal.eat()

