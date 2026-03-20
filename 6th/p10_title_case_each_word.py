def custom_rindex(s, sub):
    sub_len = len(sub)
    
    for i in range(len(s) - sub_len, -1, -1):
        if s[i:i + sub_len] == sub:
            return i
    
    return -1

text = input("Enter the string: ")
sub = input("Enter substring to find: ")
print("Result:", custom_rindex(text, sub))