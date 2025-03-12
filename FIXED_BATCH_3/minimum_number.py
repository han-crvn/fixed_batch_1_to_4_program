#Create a list
numbers_list = []

#Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = int(input("Enter the number: "))
        
        #Update the list
        numbers_list.append(number)

    except ValueError:
        print("Invalid")
        break

#Check which is the smallest number
min_number = min(numbers_list)
        
#Print the result
print(f"Result: {min_number}")