
def concatenate_lists(list1, list2):
    lst = []
    for x in list1:
        for y in list2:
            lst.append(x + y)
    return lst


# Test the function
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatenate_lists(list1, list2))
