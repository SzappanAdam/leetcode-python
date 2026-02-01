def plusOne(digits: list[int]) -> list[int]:
    """
    Adds one to the integer represented by the list of digits.
    Handles carry propagation from right to left.
    """
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


if __name__ == "__main__":
    print(plusOne([9, 9, 9]))  # [1, 0, 0, 0]