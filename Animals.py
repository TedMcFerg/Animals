class Animal:
    def __init__(self, age, condition, weight):
        self.age = age
        self.health = condition
        self. weight = weight

    def eat(self):
        self.weight += 1
        farm.food -= 1
        print("eating")