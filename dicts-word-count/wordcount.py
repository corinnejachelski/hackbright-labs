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
            word = word.strip("',.!?-#$%^&();:_/")
            word_count[word] = word_count.get(word, 0) + 1
            

    # sorted_list = sorted(word_count.items())
    # #print all key, value pairs alphabetically
    # for word, count in sorted_list:
    #     print(word, count)

    sorted_list = sorted(word_count.values())
    for value in sorted_list:
        print(value)
    

print(word_counter(sys.argv[1]))