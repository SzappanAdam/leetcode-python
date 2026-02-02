def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merges nums2 into nums1 in-place, producing a sorted array.
    nums1 has enough trailing space to hold all elements of nums2.
    """
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

merge(nums1, 3, nums2, 3)
print(nums1)  # [1, 2, 2, 3, 5, 6]