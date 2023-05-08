"""
A palindrome is a word that is symmetric: if we write it backward, the result word is the
same. For example, “HANNAH” is a palindrome, but “GAGA” is not. Write a short program
that determines whether a word is a palindrome.
"""


def is_palindrome(word: str) -> bool:
    return word[::-1] == word


class TestPalindrome:
    def test_is_palindrome_correct(self):
        word = "HANNAH"
        assert is_palindrome(word)

    def test_is_palindrome_incorrect(self):
        word = "abcxyz"
        assert is_palindrome(word) is False

    def test_is_palindrome_inverted_but_not_palindrome(self):
        word = "GAGA"
        assert is_palindrome(word) is False
