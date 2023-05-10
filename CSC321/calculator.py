class Calculator ():
  def add(self, x, y):
    return x + y

  def subtract(self, x, y):
    return y - x

  def divide (self, x, y):
    return x/y

  def sumAll(self, list):
    return sum(list)


calc = Calculator()
print(calc.add(1,3))
print(calc.sumAll([1,2,3,4,5]))
