import ure
a = 5
b = 3

print(float(a+b))
print(float(a-b))
print(float(a*b))
print(float(a/b))

# improved

is_valid = False
regex = ure.compile("^([+-]?[0-9]*[.]?[0-9]+)(\s*[\+\-\*\/]\s*)([+-]?[0-9]*[.]?[0-9]+)$")
operation = ""

while not is_valid:
    operation = input('''Enter the calculation to be performed in the form "operand1 operator operand2":\n''')
    is_valid = regex.match(operation)

splitted_operation = regex.split(operation)
a = float(splitted_operation[1])
b = float(splitted_operation[3])

if(splitted_operation[2].strip() == "+"):
    print(a+b)
if(splitted_operation[2].strip() == "-"):
    print(a-b)
if(splitted_operation[2].strip() == "*"):
    print(a*b)
if(splitted_operation[2].strip() == "/"):
    print(a/b)    


