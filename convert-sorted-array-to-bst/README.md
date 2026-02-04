Convert Sorted Array to Binary Search Tree — Python Solution

📌 Problem Description

Given an integer array nums sorted in ascending order, convert it into a height-balanced binary search tree (BST).

A height-balanced BST is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Examples

\- Input: \[-10, -3, 0, 5, 9]

Output: A height-balanced BST such as:

&nbsp;     0

&nbsp;    / \\

&nbsp;  -3   9

&nbsp;  /   /

&nbsp;-10  5





\- Input: \[1, 3]

Output: A valid BST:

&nbsp; 3

&nbsp;/

1





💡 Approach

To ensure the resulting BST is height-balanced, the algorithm always chooses the middle element of the array as the root.

Steps:

\- If the array is empty → return None

\- Select the middle element as the root

\- Recursively build the left subtree from the left half

\- Recursively build the right subtree from the right half

This guarantees that the tree remains balanced because each subtree receives roughly half of the elements.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each element is inserted exactly once.

\- Space Complexity: O(log n) on average

Due to recursion depth in a balanced tree.



📝 Code Implementation

class TreeNode:

&nbsp;   def \_\_init\_\_(self, val=0, left=None, right=None):

&nbsp;       self.val = val

&nbsp;       self.left = left

&nbsp;       self.right = right



def sortedArrayToBST(nums: list\[int]) -> TreeNode:

&nbsp;   """

&nbsp;   Converts a sorted array into a height-balanced BST.

&nbsp;   Uses a divide-and-conquer approach by selecting the middle element as root.

&nbsp;   """

&nbsp;   if not nums:

&nbsp;       return None



&nbsp;   mid = len(nums) // 2

&nbsp;   root = TreeNode(nums\[mid])

&nbsp;   root.left = sortedArrayToBST(nums\[:mid])

&nbsp;   root.right = sortedArrayToBST(nums\[mid+1:])

&nbsp;   return root



🧪 Example Usage

Here is a helper function to print the tree in level order for debugging:

from collections import deque



def print\_tree(root):

&nbsp;   if not root:

&nbsp;       print("\[]")

&nbsp;       return

&nbsp;   queue = deque(\[root])

&nbsp;   result = \[]

&nbsp;   while queue:

&nbsp;       node = queue.popleft()

&nbsp;       if node:

&nbsp;           result.append(node.val)

&nbsp;           queue.append(node.left)

&nbsp;           queue.append(node.right)

&nbsp;       else:

&nbsp;           result.append(None)

&nbsp;   print(result)



root = sortedArrayToBST(\[-10, -3, 0, 5, 9])

print\_tree(root)



📁 File Structure

convert-sorted-array-to-bst/

│

├── sorted\_array\_to\_bst.py   # Python implementation

└── README.md                # Documentation



✔️ Notes

\- This is the optimal solution for this problem.

\- The divide‑and‑conquer strategy ensures the tree is height-balanced.

\- Perfect for practicing recursion and BST fundamentals.

