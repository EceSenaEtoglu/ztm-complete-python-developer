class User:
    def attack(self):
        print("do nothing")

class Wizard(User):
    def __init__(self,x):
        self.x = x
    def attack(self):
        print("attacking with x")

class Archer(User):
    def __init__(self,y):
      self.y = y
    def attack(self):
      print("attacking with y")