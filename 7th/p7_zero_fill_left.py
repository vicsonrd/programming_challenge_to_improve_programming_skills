def custom_zfill(s, width):
    zeros_to_add = width - len(s)
    if zeros_to_add > 0:
        return '0' * zeros_to_add + s
    return s

text = input("Enter the string: ")
width = int(input("Enter width for zfill: "))
print("Result:", custom_zfill(text, width))