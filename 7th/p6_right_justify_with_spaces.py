def custom_rjust(s, width):
    spaces_to_add = width - len(s)
    if spaces_to_add > 0:
        return ' ' * spaces_to_add + s
    return s

text = input("Enter the string: ")
width = int(input("Enter width for rjust: "))
print("Result:", f"'{custom_rjust(text, width)}'")