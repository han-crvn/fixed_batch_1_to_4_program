# Create a empty list
list_of_even = []

# Create a for loop that will input up to 100
for number in range(101):
    
    # Validate the numbers if they are even and add it to the list
    if number % 2 == 0:
        list_of_even.append(number)

# Print even numbers
print(f"Even numbers are {list_of_even}.")