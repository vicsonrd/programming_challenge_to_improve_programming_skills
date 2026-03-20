def custom_lower(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

text = input("Enter the string: ")
print("Result:", custom_lower(text))