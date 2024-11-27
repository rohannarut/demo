# Initialize a list to store the 10 numbers
numbers = []

# Collect 10 numbers from the user
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Calculate the sum of the numbers
total = sum(numbers)

# Display the result
print(f"The sum of the entered numbers is: {total}")
