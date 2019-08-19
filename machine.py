import random


class Machine:
  def __init__(self, l, h):
    self.low = l
    self.high = h
    self.ans = random.randint8(l, h)

  def guess(self, g):
    if g == self.ans:
      print("猜對了")
      return True
    elif g < self.ans:
      print("猜小了")
      self.low = g
      return False
    else:
      print("猜大了")
      self.high = g
      return False

    def show(self):
      return "請輸入" + str(self.low) + "~" + str(self.high)
