# Create a lists and variable
nums = {}

# Use loop and try-except to allow users to input number and stop if the input is invalid
while True:
    try:
        number = int(input("Enter a number: "))

        if nums.get(number):
             nums[number] += 1

        else:
             nums[number] = 1
        
    except ValueError:
         break

# Check which number has the most occurences
biggest = max(nums.values())

# Print the result
for num, count in nums.items():
    if count == biggest:
        print(num)