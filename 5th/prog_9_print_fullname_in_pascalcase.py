full_name = input("Enter your full name in incorrect casing: ")
words = full_name.lower().split()
pascal_case = ''.join(word.capitalize() for word in words)
print(pascal_case)