def lengthOfLastWord(s: str) -> int:
    """
    Primary solution: scan from the end.
    Returns the length of the last word in the string.
    """
    i = len(s) - 1
    length = 0

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count characters of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length


# Alternative Pythonic solution
def lengthOfLastWord_pythonic(s: str) -> int:
    s = s.rstrip()
    return len(s.split()[-1])


if __name__ == "__main__":
    print(lengthOfLastWord("   fly me   to   the moon  "))  # 4
    print(lengthOfLastWord("Hello World"))                  # 5
    print(lengthOfLastWord("luffy is still joyboy"))        # 6