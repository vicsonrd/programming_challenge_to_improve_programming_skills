# Prog05: Display numbers sorted

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Program ends.")
        break

if numbers:
    numbers.sort()
    print("Numbers from lowest to highest:")
    for n in numbers:
        print(n)
else:
    print("No valid numbers entered.")