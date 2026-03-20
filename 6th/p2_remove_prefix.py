def custom_removeprefix(s, prefix):
    if s[:len(prefix)] == prefix:
        return s[len(prefix):]
    return s

text = input("Enter the string: ")
prefix = input("Enter prefix to remove: ")
print("Result:", custom_removeprefix(text, prefix))