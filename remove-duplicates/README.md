Remove Duplicates from Sorted Array — Python Solution

📌 Problem Description

Given a sorted integer array nums, remove the duplicates in-place such that each unique element appears only once.

The relative order of the elements must be preserved.

You must return the number of unique elements (k).

The first k elements of nums should contain the unique values in sorted order.

The remaining elements beyond index k - 1 do not matter.

Examples

\- Input: \[1,1,2] → Output: 2, array becomes \[1,2,\_]

\- Input: \[0,0,1,1,1,2,2,3,3,4] → Output: 5, array becomes \[0,1,2,3,4,\_...]



💡 Approach

The solution uses a two-pointer technique:

\- k tracks the position of the last unique element

\- i iterates through the array

For each element:

\- Compare nums\[i] with nums\[k]

\- If they differ, increment k and copy the new unique value into nums\[k]

This ensures all unique values are moved to the front of the array in-place, without extra memory.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each element is visited once.

\- Space Complexity: O(1)

No additional data structures are used.



📝 Code Implementation

def removeDuplicates(nums: list\[int]) -> int:

&nbsp;   """

&nbsp;   Removes duplicates from a sorted list in-place.

&nbsp;   Returns the number of unique elements.

&nbsp;   """

&nbsp;   if not nums:

&nbsp;       return 0



&nbsp;   k = 0



&nbsp;   for i in range(1, len(nums)):

&nbsp;       if nums\[i] != nums\[k]:

&nbsp;           k += 1

&nbsp;           nums\[k] = nums\[i]



&nbsp;   return k + 1



🧪 Example Usage

print(removeDuplicates(\[0,0,1,1,1,2,2,3,3,4]))  

\# Output: 5

\# Modified array: \[0,1,2,3,4,...]



📁 File Structure

remove-duplicates/

│

├── remove\_duplicates.py   # Python implementation

└── README.md              # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- The two-pointer technique is a common pattern in array manipulation tasks.

\- Perfect for algorithm practice and LeetCode collections.



