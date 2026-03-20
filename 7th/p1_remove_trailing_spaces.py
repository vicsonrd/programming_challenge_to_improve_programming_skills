def custom_rstrip(s):
    index = len(s) - 1
    while index >= 0 and s[index] == ' ':
        index -= 1
    return s[:index + 1]

text = input("Enter the string: ")
print("Result:", custom_rstrip(text))