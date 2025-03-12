#Create a list
numbers_list = []

#Use for loop to allow users to input 10 numbers
while True:
    try:
        number = int(input("Enter the number: "))
    
        #Update the list
        numbers_list.append(number)
    
        #Check which is the highest number
        max_number = max(numbers_list)
        
        #Print the result
        print(f"Result: {max_number}")

    except ValueError:
        print("Invalid")
        break