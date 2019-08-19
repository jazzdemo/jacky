class Person:
  name = None
  height = None
  weight = None

p1 = Person()
p1.name = "jacky"
p1.height = 170
p1.weight = 72

p2 = Person()
p2.name = "jazz"
p2.height = 175
p2.weight = 76

print(p1.weight / (p1.height / 100) ** 2)