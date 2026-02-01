def mySqrt(x: int) -> int:
    """
    Computes the integer square root of x using binary search.
    Returns the floor of the real square root.
    """
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right


if __name__ == "__main__":
    print(mySqrt(8))  # 2