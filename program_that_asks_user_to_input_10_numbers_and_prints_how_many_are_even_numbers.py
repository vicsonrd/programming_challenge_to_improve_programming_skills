count = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    
    if num % 2 == 0:
        count += 1

print("Even numbers count:", count)