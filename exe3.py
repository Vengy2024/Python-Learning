def remove_empty_strings(input_list):
    result = []
    for string in input_list:
        if string != "":
            result.append(string)
    return result


input_list = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(remove_empty_strings(input_list))