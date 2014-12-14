from rhyme_detect import syllables


def test_syllables_invalid():
    word_syllables = syllables.syllables("invalidword")

    assert len(word_syllables) == 0


def test_syllables_single():
    word_syllables = syllables.syllables("a")

    assert len(word_syllables) == 1
    assert word_syllables == ["ah"]


def test_syllables_multiple():
    word_syllables = syllables.syllables("super")

    assert len(word_syllables) == 2
    assert word_syllables == ["suw", "per"]


def test_syllables_long():
    word_syllables = syllables.syllables("circumference")

    assert len(word_syllables) == 4
    assert word_syllables == ["ser", "kah", "mfrah", "ns"]
