def count_occurrences(filename, word):
    count = 0
    print("-------------Opening the file------")
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for w in words:
                if w.lower() == word.lower():
                    count += 1

    file.close()
    return count



 # Example usage
filename = "notes.txt"
search_word = "the"

occurrences = count_occurrences(filename, search_word)
print(f"The word '{search_word}' appears {occurrences} times in '{filename}'.")
print('---------------File Closed---------')
