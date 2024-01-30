def invert_dictionary(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict


input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
print(invert_dictionary(input_dict))
