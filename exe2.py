
def concatenate_lists(list1, list2):
    lst = []
    for x in list1:
        for y in list2:
            lst.append(x + y)
    return lst



list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatenate_lists(list1, list2))
