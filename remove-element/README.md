Remove Element — Python Solution

📌 Problem Description

Given an integer array nums and an integer val, remove all occurrences of val in-place.

The order of the remaining elements may change, but the operation must be done without using extra memory.

You must return the number of elements not equal to val (k).

The first k elements of nums should contain the values that are not equal to val.

The remaining elements beyond index k - 1 do not matter.

Examples

\- Input: nums = \[3,2,2,3], val = 3 → Output: 2, array becomes \[2,2,\_]

\- Input: nums = \[0,1,2,2,3,0,4,2], val = 2 → Output: 5, array becomes \[0,1,3,0,4,\_...]



💡 Approach

The solution uses a two-pointer technique:

\- k tracks the position where the next valid (non‑val) element should be placed

\- i iterates through the array

For each element:

\- If nums\[i] is not equal to val, copy it to nums\[k]

\- Increment k

This ensures all valid elements are moved to the front of the array in-place, without allocating extra memory.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each element is visited once.

\- Space Complexity: O(1)

No additional data structures are used.



📝 Code Implementation

def removeElement(nums: list\[int], val: int) -> int:

&nbsp;   """

&nbsp;   Removes all occurrences of `val` from the list in-place.

&nbsp;   Returns the number of elements not equal to `val`.

&nbsp;   """

&nbsp;   k = 0



&nbsp;   for i in range(len(nums)):

&nbsp;       if nums\[i] != val:

&nbsp;           nums\[k] = nums\[i]

&nbsp;           k += 1



&nbsp;   return k



🧪 Example Usage

print(removeElement(\[0,1,2,2,3,0,4,2], 2))

\# Output: 5

\# Modified array: \[0,1,3,0,4,...]



📁 File Structure

remove-element/

│

├── remove\_element.py   # Python implementation

└── README.md           # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- The two-pointer technique is a common pattern in array manipulation tasks.

\- Perfect for algorithm practice and LeetCode collections.



