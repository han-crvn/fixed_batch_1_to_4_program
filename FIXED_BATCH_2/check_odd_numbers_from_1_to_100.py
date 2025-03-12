#Initialize count to 0 and create a list
count = 0
num_list = []

#Create a while loop
while count < 101:
    
    # Validate if number is odd and add it to the list
    if count % 2 != 0:
        num_list.append(count)

# Update the count
    count += 1

# Print the result
print(f"Result: {num_list}.")