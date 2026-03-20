full_name = input("Enter your full name in incorrect casing: ")
words = full_name.lower().split()
snake_case = '_'.join(words)
print(snake_case)