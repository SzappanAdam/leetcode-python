def addBinary(a: str, b: str) -> str:
    """
    Adds two binary strings and returns the result as a binary string.
    Processes digits from right to left and handles carry propagation.
    """
    result = []
    i, j = len(a) - 1, len(b) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))


if __name__ == "__main__":
    print(addBinary("11", "1"))  # "100"