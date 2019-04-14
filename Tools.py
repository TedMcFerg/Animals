
class Tool:
    def __init__(self, age, condition):
        self.age = age
        self.condition = condition

    def use(self):
        if self.condition > 0:
            self.condition -= 1
            return 1
        if self.condition == 0:
            return -1

