from rhyme_detect.utils import get_nth_word, last_word, possible_phones


def line_similarity(first_line, second_line):
    first_compare = last_word(first_line)
    second_compare = last_word(second_line)

    return word_similarity(first_compare, second_compare)

def word_similarity(first_word, second_word, start_phone=None, end_phone=None):
    first_phones = possible_phones(first_word)
    second_phones = possible_phones(second_word)

    if not first_phones or not second_phones:
        return 0

    first_phones = first_phones[0]
    second_phones = second_phones[0]

    first_range = first_phones[start_phone:end_phone]
    second_range = second_phones[start_phone:end_phone]

    first_range = first_range[::-1]
    second_range = second_range[::-1]

    if len(first_range) > len(second_range):
        first_range, second_range = second_range, first_range

    hits = 0
    total = len(first_range)

    for idx, phone in enumerate(first_range):
        other_phone = second_range[idx]

        if phone == other_phone:
            hits += 1

            # Phones with emphasis are better matches, weight them more
            if phone[-1].isdigit():
                hits += 1
                total += 1

    return hits / total
