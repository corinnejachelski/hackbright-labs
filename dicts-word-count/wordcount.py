import sys

def word_counter(file):
    """Count the number of times a word appears in a file"""

    #open file
    file = open(file)

    #create empty dictionary
    word_count = {}

    #parse through each line in file
    for line in file:
        #create list of words in line all lowercase
        words = line.rstrip().lower().split() 

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(word, count)

print(word_counter("test.txt"))