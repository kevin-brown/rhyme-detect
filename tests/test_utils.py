from rhyme_detect import utils
import pytest
import unittest


# utils.last_word

def test_last_word_blank():
    with pytest.raises(ValueError):
        utils.last_word("")


def test_last_word_punctuation():
    word = utils.last_word("punctuation.")

    assert word == "punctuation"


def test_last_word_lowercase():
    word = utils.last_word("This is an example sentence")

    assert word == "sentence"


def test_last_word_casing():
    word = utils.last_word("TESTING ALL CAPS!!!")

    assert word == "CAPS"


# utils.possible_phones

def test_possible_phones_none():
    phones = utils.possible_phones("invalidword")

    assert len(phones) == 0


def test_possible_phones_single():
    phones = utils.possible_phones("short")

    assert len(phones) == 1


def test_possible_phones_multiple():
    phones = utils.possible_phones("advantage")

    assert len(phones) == 4
