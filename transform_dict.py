def transform_dictionary(input_dict):
    transformed_dict = {}
    for key in input_dict:
        print(key)
        key_length = len(key)
        print(key_length)
        if key_length not in transformed_dict:
            transformed_dict[key_length] = [key]
        else:
            transformed_dict[key_length].append(key)
    return transformed_dict

input_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4, 'grape': 5}

transformed_dict = transform_dictionary(input_dict)
print(transformed_dict)
