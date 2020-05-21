import sys

def word_counter(file):
    """Count the number of times a word appears in a file"""

    #open file
    file = open(sys.argv[1])

    #create empty dictionary
    word_count = {}

    #parse through each line in file
    for line in file:
        #create list of words in line all lowercase
        words = line.rstrip().lower().split() 

        #parse through each word in line
        for word in words:
            #check if word is all alpha characters
            if word.isalpha():
                #append word key to dict if not present, or add 1 to present value
                word_count[word] = word_count.get(word, 0) + 1
            else:
                #strip last character in word if not all alpha
                word = word[:-1]
                #then add word key to dict if not present, or add 1 to present value
                word_count[word] = word_count.get(word, 0) + 1

    #print all key, value pairs
    for word, count in word_count.items():
        print(word, count)

(word_counter(sys.argv[1]))