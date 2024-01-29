def delete_keys(dictionary, keys_to_delete):
    result = {}
    for key in dictionary:
        if key not in keys_to_delete:
            result[key] = dictionary[key]
    return result

# Test the function
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
keys_to_delete = ["name", "age"]
print(delete_keys(sample_dict, keys_to_delete))