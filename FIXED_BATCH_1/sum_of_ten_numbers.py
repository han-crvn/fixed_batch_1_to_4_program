# Initialize the total to 0
total = 0

# Create a loop that will allow user to input 10 times
for i in range(10):
    numbers = float(input(f"Enter number {i + 1}: "))
    
    # Add the 10 numbers
    total += numbers

# Print the total sum
print(f"Total sum: {total}")