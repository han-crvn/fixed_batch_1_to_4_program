#Create empty list
list_of_even = []

#Create loop to input numbers for 10 times
for i in range(10):
    number = int(input(f"[{i + 1}] Enter the number: "))

#Validate if it is a even number and add it to the list
    if number % 2 == 0:
        list_of_even.append(number)

#Count the total number of even numbers
print(f"The total even numbers in the list is {len(list_of_even)}.")