import re

def special_char_removal(strings):
    new_string = []
    for string in strings:
        temp_string = re.sub(r'[^a-zA-Z0-9]', '', string) #regular expression sub is subsitute function
        new_string.append(temp_string)
    return new_string


input_strings = ['nB~!@#$%^23', 'Gh&*45vD9zL', 'qW@3yU%1r+7X', 'p$*8JmVcBn6F', 'k!2oT&7sPmQ"(l']
output_strings = special_char_removal(input_strings)
print(output_strings)
