# Create a empty list
not_zero = []

# Create a loop that will input 1 - 100
for number in range(101):

    # Validate if they ends with 0 and append if they are not
    if number % 10 != 0:
        not_zero.append(number)

# Print the list
print(not_zero)