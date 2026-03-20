def custom_center(s, width):
    total_spaces = width - len(s)
    if total_spaces <= 0:
        return s
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    return ' ' * left_spaces + s + ' ' * right_spaces

text = input("Enter the string: ")
width = int(input("Enter width for center: "))
print("Result:", f"'{custom_center(text, width)}'")