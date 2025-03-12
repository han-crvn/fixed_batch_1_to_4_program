#Create a list
numbers_list = []

#Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = int(input("Enter the number: "))
        
        #Update the list
        numbers_list.append(number)

#Check which is the smallest number and print it
    
    except ValueError:
        print("Invalid")
        break