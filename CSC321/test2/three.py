# A function that interchanges the first and last elements of a list
def interchange():
  _input = input("Enter a list of numbers separated by coma (,): ")
  list = _input.split(",")
  list[0], list[-1] = list[-1], list[0]
  return list

print(interchange())

