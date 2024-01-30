def lists_to_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(lists_to_dict(keys, values))