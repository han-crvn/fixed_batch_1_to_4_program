#Initialize total to 0
total = 0

#Use loop to input 10 numbers
for i in range(10):
    number = float(input(f"[{i + 1}] Enter the number: "))

    #Add the first number
    if i == 0:
        total += number

    # Subtract the remaining numbers
    else:
        total -= number
        
#Print the result