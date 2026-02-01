def climbStairs(n: int) -> int:
    """
    Returns the number of distinct ways to climb to the top.
    Uses Fibonacci logic with O(1) space.
    """
    if n <= 2:
        return n

    first, second = 1, 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


if __name__ == "__main__":
    print(climbStairs(5))  # 8