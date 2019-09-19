# import unittest
from spaceman import is_word_guessed
from spaceman import get_guessed_word
from spaceman import is_guess_in_word


def test_is_word_guessed():
    assert is_word_guessed('apple', 'apple') == True
    assert is_word_guessed('muy', 'bien') == False


def test_get_guessed_word():
    assert get_guessed_word('apple', 'apple') == 'apple'
    assert get_guessed_word('orange', 'apple') == 'a___e'


def test_is_guess_in_word():
    assert is_guess_in_word('a', 'orange') == True
    assert is_guess_in_word('o', 'apple') == False
#
# if __name__ == '__main__':
#     secret_word = load_word()
#     spaceman(secret_word)
