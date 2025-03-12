#Create an empty lists
numbers_list = []

#Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = int(input("Enter the number: "))

#Add the number to the list

#Calculate the average of the numbers in the list

#Print the result

    except ValueError:
        print("Invalid")
        break