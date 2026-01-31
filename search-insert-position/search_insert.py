def searchInsert(nums: list[int], target: int) -> int:
    """
    Returns the index where the target should be inserted in a sorted list.
    Uses binary search for O(log n) performance.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 2))  # 1