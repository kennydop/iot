def print_results(a, b):
    print(f'{a if a > b else b} is greater than {b if b < a else a}')

a = 51
b = 300

print_results(a, b)


# improved

valid = False

a = 0
b = 0

while not valid:
    integers = input("Please enter two integer numbers separated by space: ").split(" ")
    
    if len(integers) != 2:
        print("Please enter exactly 2 integers")
    else:
        try:
            a = int(integers[0])
        except:
            a = None
        
        try:
            b = int(integers[1])
        except:    
            b = None
            
        if not a and not b:
            print("Both inputs are invalid, try again!")
        elif not a:
            print("First input: %s is invalid, please repeat!" % integers[0])
        elif not b:
            print("Second input: %s is invalid, please repeat!" % integers[1])
        else:
            print_results(a, b)
            valid = True
                
                