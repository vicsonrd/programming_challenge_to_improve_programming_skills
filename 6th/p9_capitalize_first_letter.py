def custom_capitalize(s):
    if not s:
        return ''
    first_char = s[0]
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)
    result = first_char
    for char in s[1:]:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

text = input("Enter the string: ")
print("Result:", custom_capitalize(text))