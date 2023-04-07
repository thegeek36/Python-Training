"""Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary."""

def text_freq(text):
    d={}
    for i in text.lower().split():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    max_freq = 0
    max_freq_word = ""
    for word in d:
        if d[word] > max_freq:
            max_freq = d[word]
            max_freq_word = word
        elif d[word] == max_freq:
            if len(word)>len(max_freq_word):
                max_freq_word = word
    return max_freq_word + " : " + str(max_freq)

print(text_freq("Good bad good bad summer"))