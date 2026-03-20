def custom_startswith(s, prefix):
    if len(prefix) > len(s):
        return False
    return s[:len(prefix)] == prefix

text = input("Enter the string: ")
prefix = input("Enter prefix to check: ")
print("Result:", custom_startswith(text, prefix))