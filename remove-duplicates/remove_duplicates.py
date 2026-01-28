def removeDuplicates(nums: list[int]) -> int:
    """
    Removes duplicates from a sorted list in-place.
    Returns the number of unique elements.
    """
    if not nums:
        return 0

    k = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    return k + 1


if __name__ == "__main__":
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # 5