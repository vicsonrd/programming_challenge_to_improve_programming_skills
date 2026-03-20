numbers = []
while True:
    try:
        num = int(input("Enter a number (invalid to stop): "))
        numbers.append(num)
    except:
        break

if numbers:
    most_dup = max(numbers, key=lambda x: numbers.count(x))
    print("Number with most duplicates:", most_dup)
