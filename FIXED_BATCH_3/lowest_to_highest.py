# Create empty list
numbers_list = []

# Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = float(input("Enter the number: "))
        
        # Update the list
        numbers_list.append(number)

    except ValueError:
        print("Invalid")
        break

# Arrange the list from lowest to highest
arranged_number = sorted(numbers_list)
        
# Print the result
print(f"Result: {arranged_number}")