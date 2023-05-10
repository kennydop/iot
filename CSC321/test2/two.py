num = int(input("Enter a number to check: "))
if num%2 == 0 and (num**2)%2 == 0:
  print(f'{num} and {num**2} are both even numbers')
elif num%2 == 0:
  print(f'{num} is an even number but {num**2} is not')
elif (num**2)%2 == 0:
  print(f'{num} is not an even number but {num**2} is')
else:
  print(f'Both {num} and {num**2} are not even numbers')

