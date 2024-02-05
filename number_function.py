def manipulate_values(list_of_dicts):
    manipulated_dicts = []
    for dictionary in list_of_dicts:
        manipulated_dict = {}
        for key, value in dictionary.items():
            if isinstance(value, int):
                manipulated_dict[key] = value * 2
            elif isinstance(value, str):
                manipulated_dict[key] = value[::-1]  # Reverse the string
            elif isinstance(value, float):
                manipulated_dict[key] = round(value)  # Round to the nearest integer
        manipulated_dicts.append(manipulated_dict)
    return manipulated_dicts


list_of_dicts = [
    {'a': 5, 'b': 'hello', 'c': 3.14},  #'a' - Key; 5 - Value like wise
    {'x': 10, 'y': 'world', 'z': 7.5}
]

output_list_of_dicts = manipulate_values(list_of_dicts)
print("With isinstance method")
print("Input")
print(list_of_dicts)
print("Output")
print(output_list_of_dicts)
# without using isinstance function

def manipulate_values(list_of_dicts):
    manipulated_dicts = []
    for dictionary in list_of_dicts:
        manipulated_dict = {}
        for key, value in dictionary.items():
            value_type = type(value)
            if value_type == int:
                manipulated_dict[key] = value * 2
            elif value_type == str:
                manipulated_dict[key] = value[::-1]  # Reverse the string using comprehensive method of string reverse
            elif value_type == float:
                manipulated_dict[key] = round(value)  # Round to the nearest integer
            else:
                manipulated_dict[key] = value  # Keep the original value if not int, str, or float
        manipulated_dicts.append(manipulated_dict)
    return manipulated_dicts

list_of_dicts = [
    {'a': 5, 'b': 'hello', 'c': 3.14},
    {'x': 10, 'y': 'world', 'z': 7.5}
]

output_list_of_dicts = manipulate_values(list_of_dicts)
print("Without isinstance method")
print("Input")
print(list_of_dicts)
print("Output")
print(output_list_of_dicts)