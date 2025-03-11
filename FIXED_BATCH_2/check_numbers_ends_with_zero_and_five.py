#Create empty list
num_list = []

#Use for loop to input 1 - 100
for number in range(101):
    
    #Validate if number ends with 0 or 5 and add if they are not
    if number % 5 != 0:
        num_list.append(number)

# Print result
print(f"Result: {num_list}.")