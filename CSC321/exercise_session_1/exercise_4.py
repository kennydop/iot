def fib(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    
    return fib(n-1) + fib(n-2)



def fib_with_max(n, _max):
    if(_max < 1):
        return 0
    if(n == 0 or _max == 0):
        return 0
    if(n == 1  or _max == 1):
        return 1
    
    return fib_with_max(n-1, _max - 1) + fib_with_max(n-2, _max - 2)
    

fib_valid = False
while not fib_valid:
    try:
        n = int(input("Enter a positive integer n: "))
        if(0 <= n <= 20):
            print(fib(n))
            fib_valid = True
        else:
            print("Number should be in the range [0 - 20]")
    except:
        print("Input a valid positive integer")
        
fib_with_max_valid = False
while not fib_with_max_valid:
    try:
        n = int(input("Enter a positive integer n: "))
        _max = int(input("Enter the maximum value you wish to calculate: "))
        if(0 <= n <= _max):
            print(fib_with_max(n, 10))
            fib_with_max = True
        else:
            print("Number should be in the range [0 - %s]" % _max)
    except:
        print("Input a valid positive integer")
