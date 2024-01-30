def square_for_loop(number):
    squared_list = []
    for num in number:
        squared_list.append(num ** 2)
    return squared_list


numbers = [1, 2, 3, 4, 5]
print("Using for loop:", square_for_loop(numbers))
