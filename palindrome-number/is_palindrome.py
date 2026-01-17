def is_palindrome(x: int) -> bool:
    """
    Returns True if x is a palindrome number.
    Negative numbers are not considered palindromes.
    """
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


if __name__ == "__main__":
    print(is_palindrome(121))
    print(is_palindrome(-121))
    print(is_palindrome(10))
    print(is_palindrome(123454321))