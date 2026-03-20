numbers = []
while True:
    try:
        num = int(input("Enter a number (invalid to stop): "))
        numbers.append(num)
    except:
        break

if numbers:
    print("Highest number:", max(numbers))
