numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

duplicates = set([x for x in numbers if numbers.count(x) > 1])
print("Duplicate numbers:", duplicates)
