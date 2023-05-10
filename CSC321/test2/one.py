#This script collects information about a user utilizing all primitive data types

name = input("What is your name: ")
age = int(input("How old are you (years): "))
gender = input("Enter your gender: ")
trans_char = input("Are you a transgender (Enter Y for yes or N for no): ")
trans = True if trans_char == "Y" else False
height = float(input("Enter your height (cm): "))

print("\nName: ", name)
print("Age: ", age)
print("Gender: ", gender)
print("Transgender: ", trans)
print("Height: ", height)
