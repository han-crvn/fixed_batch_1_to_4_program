#Create a list
numbers_list = []
most_number = None
max_count = 0

#Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = int(input("Enter the number: "))

        #Update the list
        numbers_list.append(number)

        #Check which number has the most occurences
        if numbers_list.count(number) > max_count:
            max_count = numbers_list.count(number)
            most_number = number

        #Print the result
        print(f"Result: {most_number} = {max_count}")

    except ValueError:
        print("Invalid")
        break