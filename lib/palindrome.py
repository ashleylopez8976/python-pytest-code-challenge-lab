def longest_palindromic_substring(s):
    """
    Return the longest palindromic substring of s.
    Return an empty string when s is empty.
    """
    if len(s) < 2:
        return s

    start = 0
    max_length = 1

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - left - 1

    for i in range(len(s)):
        for left, right in ((i, i), (i, i + 1)):
            palindrome_start, length = expand(left, right)

            if length > max_length:
                start = palindrome_start
                max_length = length

    return s[start:start + max_length]