def removeElement(nums: list[int], val: int) -> int:
    """
    Removes all occurrences of `val` from the list in-place.
    Returns the number of elements not equal to `val`.
    """
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


if __name__ == "__main__":
    print(removeElement([0,1,2,2,3,0,4,2], 2))  # 5