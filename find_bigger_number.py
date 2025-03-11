#Create a program that ask user to input 2 numbers. Print the bigger number.

#Input the numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the first number: "))

#Validate which is bigger and print it
if number_1 > number_2:
    print(F"Bigger number: {number_1}")
elif number_2 > number_1:
    print(F"Bigger number: {number_1}")
else:
    print("They are both equal")