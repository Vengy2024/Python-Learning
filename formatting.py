import re
def manipulate_values(input_dict):
    output_dict = {}
    output_dict1 = {}
    for key, value in input_dict.items():
        reversed_value = value[::-1]
        if value == reversed_value:
            output_dict[key] = f"{reversed_value} - palindrome"
        elif value != reversed_value:
            output_dict[key] = {reversed_value}
    for key, value in output_dict.items():
        if isinstance(value, str):
            value = {value}
        modified_values = []
        for val in value:
            # Check if 'e' or 'E' exists in the value
            if 'e' in val or 'E' in val:
                # Replace 'e' or 'E' with '*'
                modified_val = val.replace('e', '*').replace('E', '*')
                modified_values.append(modified_val)
            else:
                modified_values.append(val)
        output_dict[key] = modified_values

    return output_dict

input_dict = {
    'word1': 'hello',
    'word2': 'level',
    'word3': 'example',
    'word4': 'racecar'
}

output_dict = manipulate_values(input_dict)
print(output_dict)
