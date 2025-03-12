# Create an empty lists
numbers_list =[]
duplicate_numbers = []

# Use for loop to allow user to input 10 numbers
for i in range(10):
    number = float(input(f"[{i + 1}] Enter the number: "))

    # Add the numbers in the list
    numbers_list.append(number)

# Use loop to check the occurences of numbers
for number in numbers_list:
    if numbers_list.count(number) != 1:
        duplicate_numbers.append(number)

# Print the result
print(f"Result: {duplicate_numbers}")