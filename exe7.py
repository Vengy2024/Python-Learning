def max_value_key(dictionary):
    max_value = -1 # Initialize max_value to negative infinity
    max_key = None  # Initialize max_key to None
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

my_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}
print(max_value_key(my_dict))


#using max funtion

def max_value_key(dictionary):
    return max(dictionary, key=dictionary.get)

my_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}
print(max_value_key(my_dict))
