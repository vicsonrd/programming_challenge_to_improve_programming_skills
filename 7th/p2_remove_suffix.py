def custom_removesuffix(s, suffix):
    if s[-len(suffix):] == suffix:
        return s[:-len(suffix)]
    return s

text = input("Enter the string: ")
suffix = input("Enter suffix to remove: ")
print("Result:", custom_removesuffix(text, suffix))