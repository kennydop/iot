def sine(x):
    return (4*x*(180 - x))/(40500 - x*(190 - x))

def print_err():
    print("Please enter a valid number in degrees [1 - 360]")

valid = False
while not valid:
    try:
        num = float(input("Enter a degree to calculate it's sine: "))
        if(0 > num > 360):
            print_err()
        else:
            print(sine(num))
            valid = True
    except:
        print_err()
    
