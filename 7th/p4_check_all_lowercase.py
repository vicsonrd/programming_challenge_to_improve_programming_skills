def custom_islower(s):
    for char in s:
        if 'A' <= char <= 'Z':
            return False
    return True

text = input("Enter the string: ")
print("Result:", custom_islower(text))