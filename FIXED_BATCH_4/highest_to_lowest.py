#Create empty list
numbers_list = []

#Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = int(input("Enter the number: "))

        #Update the list
        numbers_list.append(number)

        #Arrange the list from highest to lowest
        arranged_number = sorted(numbers_list)
        arranged_number.reverse()
        
        #Print the result
        print(f"Result: {arranged_number}")
    
    except ValueError:
        print("Invalid")
        break