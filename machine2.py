import machine

m = machine.Machine(1, 100)
while True:
  g = int(input(m.show()))
  if m.guess(g) == True:
    break