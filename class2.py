class Person:

  def __init__(self, n, h, w):
    self.name = n
    self.height = h
    self.weight = w

  def bmi(self):
    return self.weight / (self.height / 100) ** 2

p1 = Person("jacky", 170, 72)
p2 = Person("jazz", 175, 75)
print(p1.bmi())
print(p2.bmi())