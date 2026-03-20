# Program to count even numbers among 10 inputs

# Initialize counter
even_count = 0

# Loop to get 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

# Print result
print(f"There are {even_count} even numbers.")