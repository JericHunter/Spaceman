import unittest
from spaceman import is_word_guessed
from spaceman import get_guessed_word
from spaceman import is_guess_in_word


class getWord(unittest.TestCase):
    def t_is_word_guessed(self):
        assert is_word_guessed('apple', 'apple') is True
        assert is_word_guessed('muy', 'bien') is False

    def t_get_guessed_word(self):
        assert get_guessed_word('apple', 'apple') == 'apple'
        assert get_guessed_word('orange', 'apple') == 'a___e'

    def t_is_guess_in_word(self):
        assert is_guess_in_word('a', 'orange') is True
        assert is_guess_in_word('o', 'apple') is False


if __name__ == '__main__':
    unittest.main()
