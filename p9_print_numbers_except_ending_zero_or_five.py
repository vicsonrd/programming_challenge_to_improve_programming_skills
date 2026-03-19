# Program to print numbers from 0 to 100
# excluding those ending in 0 or 5

num = 0

while num <= 100:
    # Check if last digit is not 0 or 5
    if num % 10 != 0 and num % 10 != 5:
        print(num)
    num += 1