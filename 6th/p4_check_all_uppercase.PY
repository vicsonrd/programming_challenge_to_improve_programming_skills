def custom_isupper(s):
    for char in s:
        if 'a' <= char <= 'z':
            return False
    return True

text = input("Enter the string: ")
print("Result:", custom_isupper(text))