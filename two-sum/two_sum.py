def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Returns the indices of two numbers in `nums` that add up to `target`.
    Uses a hash map for O(n) time complexity.
    """
    seen = {} 

    for index, num in enumerate(nums):
        complement = target - num 
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6)) 
    print(two_sum([3, 3], 6)) 