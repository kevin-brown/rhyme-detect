from rhyme_detect import scheme


def test_from_lines_exact():
    lines = [
        "My mistress' eyes are nothing like the sun",
        "My mistress' eyes are nothing like the sun",
    ]

    rhyme_scheme = scheme.from_lines(lines)
    expected_scheme = ["A", "A", ]

    assert rhyme_scheme == expected_scheme


def test_from_lines_similar():
    lines = [
        "My mistress' eyes are nothing like the sun",
        "If snow be white, why then her breasts are dun",
    ]

    rhyme_scheme = scheme.from_lines(lines)
    expected_scheme = ["A", "A", ]

    assert rhyme_scheme == expected_scheme


def test_from_lines_not_similar():
    lines = [
        "My mistress' eyes are nothing like the sun",
        "Coral is far more red than her lips' red",
    ]

    rhyme_scheme = scheme.from_lines(lines)
    expected_scheme = [None, None, ]

    assert rhyme_scheme == expected_scheme


def test_from_lines_single_quatrain():
    lines = [
        "My mistress' eyes are nothing like the sun",
        "Coral is far more red than her lips' red",
        "If snow be white, why then her breasts are dun",
        "If hairs be wires, black wires grow on her head",
    ]

    rhyme_scheme = scheme.from_lines(lines)
    expected_scheme = ["A", "B", "A", "B", ]

    assert rhyme_scheme == expected_scheme


def test_from_lines_multiple_quatrain():
    lines = [
        "My mistress' eyes are nothing like the sun",
        "Coral is far more red than her lips' red",
        "If snow be white, why then her breasts are dun",
        "If hairs be wires, black wires grow on her head",

        "I have seen roses damask'd, red and white",
        "But no such roses see I in her cheeks",
        "And in some perfumes is there more delight",
        "Than in the breath that from my mistress reeks",
    ]

    rhyme_scheme = scheme.from_lines(lines)
    expected_scheme = [
        "A", "B", "A", "B",
        "C", "D", "C", "D",
    ]

    assert rhyme_scheme == expected_scheme


def test_from_lines_shakespeare_sonnet():
    lines = [
        "My mistress' eyes are nothing like the sun",
        "Coral is far more red than her lips' red",
        "If snow be white, why then her breasts are dun",
        "If hairs be wires, black wires grow on her head",

        "I have seen roses damask'd, red and white",
        "But no such roses see I in her cheeks",
        "And in some perfumes is there more delight",
        "Than in the breath that from my mistress reeks",

        "I love to hear her speak, yet well I know",
        "That music hath a far more pleasing sound",
        "I grant I never saw a goddess go",
        "My mistress, when she walks, treads on the ground",

        "And yet, by heaven, I think my love as rare",
        "As any she belied with false compare",
    ]

    rhyme_scheme = scheme.from_lines(lines)
    expected_scheme = [
        "A", "B", "A", "B",
        "C", "D", "C", "D",
        "E", "F", "E", "F",
        "G", "G",
    ]

    assert rhyme_scheme == expected_scheme
