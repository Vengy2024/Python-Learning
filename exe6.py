def char_count_dict(strings):
    char_count = {}
    for char in strings:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

string = 'test'
print('Input string:', string)
print(char_count_dict(string))