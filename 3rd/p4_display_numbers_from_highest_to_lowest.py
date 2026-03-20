numbers = []
while True:
    try:
        num = int(input("Enter a number (invalid to stop): "))
        numbers.append(num)
    except:
        break

numbers.sort(reverse=True)
print("Numbers from highest to lowest:", numbers)
