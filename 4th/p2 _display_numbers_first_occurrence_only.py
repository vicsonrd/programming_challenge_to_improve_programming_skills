# Program to input 10 numbers and display only first occurrence of duplicates

numbers = []

# Ask user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nNumbers (duplicates shown only once):")
seen = set()
for n in numbers:
    if n not in seen:
        print(n)
        seen.add(n)