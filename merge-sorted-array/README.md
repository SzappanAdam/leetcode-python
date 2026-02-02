Merge Sorted Array — Python Solution

📌 Problem Description

You are given two sorted integer arrays:

\- nums1 with length m + n, where the first m elements are valid and the last n are placeholders (0s)

\- nums2 with length n

Your task is to merge nums2 into nums1 in-place, producing one sorted array.

The final array must remain in nums1, and the function should not return anything.

Examples

\- Input:

nums1 = \[1,2,3,0,0,0], m = 3

nums2 = \[2,5,6], n = 3

Output:

nums1 = \[1,2,2,3,5,6]



💡 Approach

The key insight is to merge the arrays from the end.

Since nums1 has empty space at the back, we can fill it starting from the largest values.

Pointers:

\- i = m - 1 → last valid element in nums1

\- j = n - 1 → last element in nums2

\- k = m + n - 1 → last position in nums1

Algorithm:

\- Compare nums1\[i] and nums2\[j]

\- Place the larger one at position k

\- Move the corresponding pointer backward

\- Continue until all elements of nums2 are placed

This avoids shifting elements and achieves optimal performance.



🧠 Time \& Space Complexity

\- Time Complexity: O(m + n)

Each element is processed once.

\- Space Complexity: O(1)

Everything is done in-place.



📝 Code Implementation

def merge(nums1: list\[int], m: int, nums2: list\[int], n: int) -> None:

&nbsp;   """

&nbsp;   Merges nums2 into nums1 in-place, producing a sorted array.

&nbsp;   nums1 has enough trailing space to hold all elements of nums2.

&nbsp;   """

&nbsp;   i, j, k = m - 1, n - 1, m + n - 1



&nbsp;   while j >= 0:

&nbsp;       if i >= 0 and nums1\[i] > nums2\[j]:

&nbsp;           nums1\[k] = nums1\[i]

&nbsp;           i -= 1

&nbsp;       else:

&nbsp;           nums1\[k] = nums2\[j]

&nbsp;           j -= 1

&nbsp;       k -= 1



🧪 Example Usage

nums1 = \[1,2,3,0,0,0]

nums2 = \[2,5,6]



merge(nums1, 3, nums2, 3)

print(nums1)  # \[1, 2, 2, 3, 5, 6]



📁 File Structure

merge-sorted-array/

│

├── merge\_sorted\_array.py   # Python implementation

└── README.md               # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- Merging from the back avoids unnecessary shifting.

\- Perfect for algorithm practice and LeetCode collections.

