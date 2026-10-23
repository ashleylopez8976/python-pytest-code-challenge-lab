import pytest

from palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "text, expected",
    [
        ("babad", {"bab", "aba"}),       # Multiple valid answers
        ("cbbd", {"bb"}),               # Even-length palindrome
        ("a", {"a"}),                   # Single character
        ("ac", {"a", "c"}),             # No palindrome longer than one
        ("racecar", {"racecar"}),       # Entire string
        ("", {""}),                     # Empty string
        ("aaaa", {"aaaa"}),             # Repeated characters
        ("abcba", {"abcba"}),           # Odd-length palindrome
        ("abccba", {"abccba"}),         # Even-length entire string
        ("racecarxyz", {"racecar"}),    # Palindrome at the beginning
        ("xyzracecar", {"racecar"}),    # Palindrome at the end
        ("1234321", {"1234321"}),       # Digits
        ("a" * 1000, {"a" * 1000}),     # Maximum specified length
    ],
)
def test_longest_palindromic_substring(text, expected):
    result = longest_palindromic_substring(text)

    assert result in expected