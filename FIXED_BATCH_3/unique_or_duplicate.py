# Create empty list
numbers_list = []

# Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = float(input("Enter the number: "))
        
        # Validate if the number is in the list and print the result
        if number not in numbers_list:
            print("Unique")
        else:
            print("Duplicate")
        
        # Add the number to update the list
        numbers_list.append(number)

    except ValueError:
        print("Invalid")
        break