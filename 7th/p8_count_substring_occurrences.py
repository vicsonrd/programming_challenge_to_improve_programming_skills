def custom_count(s, sub):
    count = 0
    sub_len = len(sub)
    
    for i in range(len(s) - sub_len + 1):
        if s[i:i + sub_len] == sub:
            count += 1
    
    return count

text = input("Enter the string: ")
sub = input("Enter substring to count: ")
print("Result:", custom_count(text, sub))