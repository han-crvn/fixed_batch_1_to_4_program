# Create a empty list
list_of_odds = []

# Create a loop the will allow users to input 10 numbers
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))

    # Add a condition that will check and add the odd number to the list
    if number % 2 != 0:
         list_of_odds.append(number)

# Print the number of odd numbers in the list
print(f"The number of odd numbers is {len(list_of_odds)}.")