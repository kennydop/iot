class Language():
  def __init__(self, name, static, year_released, documentation):
    self.name = name
    self.static = static
    self.year_released = year_released
    self.documentation = documentation



kennyscript = Language("kennyscript", False, 2025, "https//:docs.kennyscript.com")

print(kennyscript.static)
print(kennyscript.documentation)
print(type(kennyscript.year_released))
