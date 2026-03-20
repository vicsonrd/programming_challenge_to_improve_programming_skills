def custom_ljust(s, width):
    spaces_to_add = width - len(s)
    if spaces_to_add > 0:
        return s + ' ' * spaces_to_add
    return s

text = input("Enter the string: ")
width = int(input("Enter width for ljust: "))
print("Result:", f"'{custom_ljust(text, width)}'")