def custom_endswith(s, suffix):
    if len(suffix) > len(s):
        return False
    return s[-len(suffix):] == suffix

text = input("Enter the string: ")
suffix = input("Enter suffix to check: ")
print("Result:", custom_endswith(text, suffix))