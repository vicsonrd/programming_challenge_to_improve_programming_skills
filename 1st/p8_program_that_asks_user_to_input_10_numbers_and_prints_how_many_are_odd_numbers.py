count = 0

for i in range(10):
    num = int(input("Enter a number: "))
    
    if num % 2 != 0:
        count = count + 1

print("Total odd numbers:", count)