# Program to input 10 numbers and display non-duplicates

numbers = []

# Ask user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nNumbers without duplicates:")
unique_numbers = [n for n in numbers if numbers.count(n) == 1]

if unique_numbers:
    for n in unique_numbers:
        print(n)
else:
    print("No unique numbers found.")