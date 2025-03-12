# Create empty list
number_between = []

# Input 2 numbers
number_1 = int(input("Enter 1st number: "))
number_2 = int(input("Enter 2nd number: "))

# Check if there is a number between the two numbers
if abs(number_1 - number_2) > 1:
    
    # Check which is smaller between two numbers and using for loop add the number in between to the list and print it
    if number_1 < number_2:
        for number in range(number_1 + 1, number_2):
            number_between.append(number)
    else:
        for number in range(number_2 + 1, number_1):
            number_between.append(number)

    print(f"The number between {number_1} and {number_2}: {number_between}")

else:
    print(f"There is no number between {number_1} and {number_2}.")
