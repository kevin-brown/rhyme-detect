from rhyme_detect import rhymes


def test_line_similarity_exact():
    first_line = "My mistress' eyes are nothing like the sun"
    second_line = "My mistress' eyes are nothing like the sun"

    index = rhymes.line_similarity(first_line, second_line)

    assert index == 1


def test_line_similarity_similar():
    first_line = "My mistress' eyes are nothing like the sun"
    second_line = "If snow be white, why then her breasts are dun"

    index = rhymes.line_similarity(first_line, second_line)

    assert index == 2/3


def test_line_similarity_far():
    first_line = "My mistress' eyes are nothing like the sun"
    second_line = "Coral is far more red than her lips' red"

    index = rhymes.line_similarity(first_line, second_line)

    assert index == 0


def test_word_similarity_exact():
    index = rhymes.word_similarity("test", "test")

    assert index == 1


def test_word_similarity_close():
    index = rhymes.word_similarity("test", "best")

    assert index == 3/4


def test_word_similarity_start():
    index = rhymes.word_similarity("blurt", "blurb", end_phone=2)

    assert index == 1


def test_word_similarity_end():
    index = rhymes.word_similarity("test", "best", start_phone=-2)

    assert index == 1


def test_word_similarity_far():
    index = rhymes.word_similarity("test", "nothing")

    assert index == 0
