def display_words(filename):
    with open(filename, 'r') as file:
            for line in file:
                # Split the line into words
                words = line.split()
                # Iterate through words
                for word in words:
                    # Display words less than 4 characters
                    if len(word) < 4:
                        print(word)
    file.close()
filename = "story.txt"
display_words(filename)
