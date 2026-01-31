Search Insert Position — Python Solution

📌 Problem Description

Given a sorted array of distinct integers nums and an integer target, return the index where the target should be inserted to maintain sorted order.

If the target is found in the array, return its index.

If not, return the index where it would be inserted.

Examples

\- Input: nums = \[1,3,5,6], target = 5 → Output: 2

\- Input: nums = \[1,3,5,6], target = 2 → Output: 1

\- Input: nums = \[1,3,5,6], target = 7 → Output: 4

\- Input: nums = \[1,3,5,6], target = 0 → Output: 0



💡 Approach

The solution uses binary search to achieve O(log n) time complexity.

Steps:

\- Initialize two pointers: left = 0, right = len(nums) - 1

\- Compute the midpoint mid

\- If nums\[mid] == target, return mid

\- If nums\[mid] < target, search the right half

\- Otherwise, search the left half

\- When the loop ends, left will be the correct insertion index

This is the optimal and expected solution for this problem.



🧠 Time \& Space Complexity

\- Time Complexity: O(log n)

Binary search halves the search space each step.

\- Space Complexity: O(1)

Only a few variables are used.



📝 Code Implementation

def searchInsert(nums: list\[int], target: int) -> int:

&nbsp;   """

&nbsp;   Returns the index where the target should be inserted in a sorted list.

&nbsp;   Uses binary search for O(log n) performance.

&nbsp;   """

&nbsp;   left, right = 0, len(nums) - 1



&nbsp;   while left <= right:

&nbsp;       mid = (left + right) // 2



&nbsp;       if nums\[mid] == target:

&nbsp;           return mid

&nbsp;       elif nums\[mid] < target:

&nbsp;           left = mid + 1

&nbsp;       else:

&nbsp;           right = mid - 1



&nbsp;   return left



🧪 Example Usage

print(searchInsert(\[1,3,5,6], 2))  # Output: 1

print(searchInsert(\[1,3,5,6], 5))  # Output: 2

print(searchInsert(\[1,3,5,6], 7))  # Output: 4

print(searchInsert(\[1,3,5,6], 0))  # Output: 0



📁 File Structure

search-insert-position/

│

├── search\_insert.py   # Python implementation

└── README.md          # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- Binary search is a fundamental technique for sorted arrays.

\- Perfect for algorithm practice and LeetCode collections.



