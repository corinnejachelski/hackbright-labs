"""Generate Markov text from text files."""

import random
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read() #change to sys.argv[1]

    words = file.split()

    return words


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = open_and_read_file(sys.argv[1])

    for word in range(len(words) - 1):

        if word < (len(words) - 2):
            bigram = words[word], words[word + 1]
            next_word = words[word + 2]
    
            chains[bigram] = chains.get(bigram, []) + [next_word]   

        else:
            bigram = words[word], words[word + 1]
            chains[bigram] = chains.get(bigram, []) + ["None"]

    return chains


def make_text(arg):
    """Return text from chains."""

    chains = make_chains(arg)

    random_key = random.choice(list(chains.keys()))
    output = [random_key[0], random_key[1]]
    next_word = random.choice(chains[random_key])

    while next_word is not "None":
        random_key = (random_key[1], next_word)
        output.append(next_word)
        next_word = random.choice(chains[random_key])

    return " ".join(output)

print(make_text(sys.argv[1]))
