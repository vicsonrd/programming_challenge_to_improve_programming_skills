# Program to print all numbers between two inputs

# Ask user for two numbers
num1 = int(input("Enter_the_first_number: "))
num2 = int(input("Enter the second number: "))

# Ensure we print numbers in the correct order
start = min(num1, num2)
end = max(num1, num2)

print(f"Numbers_between {start} and {end}:")

# Loop through the range
for i in range(start + 1, end):
    print(i)