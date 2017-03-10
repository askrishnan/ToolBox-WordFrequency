""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import requests
from pickle import load, dump


little_women_text = requests.get('http://www.gutenberg.org/cache/epub/514/pg514.txt').text
f = open('littlewomen.txt', 'wb')
dump(little_women_text, f)
f.close()


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r', encoding='utf-8', errors='ignore')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    fin_line = 0
    while lines[fin_line].find('End of the Project Gutenberg EBook of Little Women, by Louisa May Alcott') == -1:
        fin_line += 1
    lines = lines[curr_line+1:fin_line-1]
    word_list = str.lower(' '.join(lines))
    word_list = word_list.split()

    for word in word_list:
        if word in string.punctuation:
            word_list.remove(word)
    return word_list


def get_top_n_words(word_list, n):
    """ Takes a file name as input, generates a word list using get_word_list() and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_counts = dict()
    for word in word_list:
        frequency = word_counts.get(word, 1)
        word_counts[word] = frequency + 1
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
    return ordered_by_frequency[0:n]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('littlewomen.txt')
    print(get_top_n_words(word_list, 100))
