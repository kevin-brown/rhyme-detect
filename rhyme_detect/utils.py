from nltk.tokenize import RegexpTokenizer
import nltk


def get_nth_word(line, position):
    tokenizer = RegexpTokenizer(r"\w+")
    words = tokenizer.tokenize(line)

    if not words:
        raise ValueError("The given line must not be empty")

    return words[position]


def last_word(line):
    return get_nth_word(line, -1)


def possible_phones(word):
    phone_dictionary = nltk.corpus.cmudict.dict()

    if word not in phone_dictionary:
        return []

    return phone_dictionary[word]
