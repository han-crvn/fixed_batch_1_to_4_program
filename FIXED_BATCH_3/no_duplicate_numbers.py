# Create a empty list
number_list = []

# Use for loop to allow users to input 10 numbers
for i in range(10):
    number = float(input(f"[{i + 1}] Enter the number: "))

    # Check if the number are not in the list and add them
    if number not in number_list:
        number_list.append(number)

# Print result
print(f"Result: {number_list}")

  