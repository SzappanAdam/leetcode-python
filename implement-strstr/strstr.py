def strStr(haystack: str, needle: str) -> int:
    """
    Primary solution: sliding window substring search.
    Returns the index of the first occurrence of `needle` in `haystack`,
    or -1 if `needle` is not found.
    """
    m, n = len(needle), len(haystack)

    if m == 0:
        return 0

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1

# Alternative Pythonic solution:
def strStr_pythonic(haystack: str, needle: str) -> int:
    """
    Alternative solution using Python's built-in string method.
    """
    return haystack.find(needle)


if __name__ == "__main__":
    print(strStr("sadbutsad", "sad"))       # 0
    print(strStr("leetcode", "leeto"))      # -1
    print(strStr("hello", "ll"))            # 2
    print(strStr_pythonic("sadbutsad", "sad"))  # 0