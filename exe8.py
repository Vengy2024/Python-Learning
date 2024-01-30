def count_word_frequency(sentence):
    words = sentence.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


sentence = "This is a sample sentence. This sentence has words."
print(count_word_frequency(sentence))