#Input the numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

#Validate which is bigger and print it
if number_1 > number_2:
    print(f"Bigger number: {number_1}")
elif number_2 > number_1:
    print(f"Bigger number: {number_2}")
else:
    print("They are both equal")