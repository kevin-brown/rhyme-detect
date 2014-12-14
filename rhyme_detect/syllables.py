from rhyme_detect.utils import possible_phones
import nltk


def syllables(word):
    phones_list = possible_phones(word)

    if not phones_list:
        return []

    phones = phones_list[0]

    syllables = []
    syllable = ""

    for phone in phones:
        if phone[-1].isdigit():
            syllable += phone[:-1].lower()
            syllables.append(syllable)
            syllable = ""
        else:
            syllable += phone.lower()

    if syllable:
        syllables.append(syllable)

    return syllables
