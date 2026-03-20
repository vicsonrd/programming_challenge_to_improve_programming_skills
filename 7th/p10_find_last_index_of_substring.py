def p10_find_last_index_of_substring():
    text = input("Enter string: ")
    sub = input("Enter substring: ")
    sub_len = len(sub)

    for i in range(len(text) - sub_len, -1, -1):
        if text[i:i + sub_len] == sub:
            print("Result:", i)
            return

    print("Result: -1")

p10_find_last_index_of_substring()