# Input 2 numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# Validate which is smaller and print it
if number_1 < number_2:
    print(f"{number_1} is the smaller number.") 
elif number_2 < number_1:
    print(f"{number_2} is the smaller number.")
else:
    print("Both are equal.")