def custom_upper(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

text = input("Enter the string: ")
print("Result:", custom_upper(text))