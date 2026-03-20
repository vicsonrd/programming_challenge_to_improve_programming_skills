def custom_lstrip(s):
    index = 0
    while index < len(s) and s[index] == ' ':
        index += 1
    return s[index:]

text = input("Enter the string: ")
print("Result:", custom_lstrip(text))