# Create a lists and variable
numbers_list = []
most_number = []
max_count = 0

# Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = float(input("Enter the number: "))

        # Update the list
        numbers_list.append(number)

    except ValueError:
        print("Invalid")
        break

# Check which number has the most occurences
for number in numbers_list:
        count = numbers_list.count(number)
        if count > max_count:
            max_count = count
            most_frequent = [number]
        elif count == max_count and number not in most_frequent:
            most_frequent.append(number)

# Print the result
print(f"Results: {most_frequent} (occurs: {max_count})")