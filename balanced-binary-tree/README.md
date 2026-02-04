Balanced Binary Tree — Python Solution

📌 Problem Description

Given the root of a binary tree, determine whether it is height-balanced.

A binary tree is height-balanced if, for every node:

|\\mathrm{height(left)}-\\mathrm{height(right)}|\\leq 1

Examples

\- Input: \[3,9,20,None,None,15,7]

Output: True

\- Input: \[1,2,2,3,3,None,None,4,4]

Output: False

\- Input: \[]

Output: True



💡 Approach

The key idea is to compute the height of each subtree bottom‑up while simultaneously checking whether it is balanced.

A helper function check(node) returns:

\- the height of the subtree if it is balanced

\- -1 if it is not balanced

This allows the algorithm to stop early as soon as an imbalance is detected.

Steps:

\- If the node is None, return height 0

\- Recursively compute the height of the left subtree

\- If the left subtree is unbalanced (-1), propagate -1 upward

\- Do the same for the right subtree

\- If the height difference is more than 1, return -1

\- Otherwise, return the subtree height

The tree is balanced if the final result is not -1.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each node is visited once.

\- Space Complexity:

\- O(h) recursion depth

\- Worst case (skewed tree): O(n)

\- Best case (balanced tree): O(log n)



📝 Code Implementation

class TreeNode:

&nbsp;   def \_\_init\_\_(self, val=0, left=None, right=None):

&nbsp;       self.val = val

&nbsp;       self.left = left

&nbsp;       self.right = right



def isBalanced(root: TreeNode) -> bool:

&nbsp;   """

&nbsp;   Determines whether a binary tree is height-balanced.

&nbsp;   Uses a bottom-up DFS that returns -1 when imbalance is detected.

&nbsp;   """

&nbsp;   def check(node):

&nbsp;       if not node:

&nbsp;           return 0



&nbsp;       left = check(node.left)

&nbsp;       if left == -1:

&nbsp;           return -1



&nbsp;       right = check(node.right)

&nbsp;       if right == -1:

&nbsp;           return -1



&nbsp;       if abs(left - right) > 1:

&nbsp;           return -1



&nbsp;       return max(left, right) + 1



&nbsp;   return check(root) != -1



🧪 Example Usage

LeetCode uses a TreeNode structure, so here is a helper to build trees from list input:

from collections import deque



def build\_tree(values):

&nbsp;   if not values:

&nbsp;       return None

&nbsp;   root = TreeNode(values\[0])

&nbsp;   queue = deque(\[root])

&nbsp;   i = 1



&nbsp;   while queue and i < len(values):

&nbsp;       node = queue.popleft()



&nbsp;       if values\[i] is not None:

&nbsp;           node.left = TreeNode(values\[i])

&nbsp;           queue.append(node.left)

&nbsp;       i += 1



&nbsp;       if i < len(values) and values\[i] is not None:

&nbsp;           node.right = TreeNode(values\[i])

&nbsp;           queue.append(node.right)

&nbsp;       i += 1



&nbsp;   return root



root = build\_tree(\[3,9,20,None,None,15,7])

print(isBalanced(root))  # True



📁 File Structure

balanced-binary-tree/

│

├── is\_balanced.py   # Python implementation

└── README.md        # Documentation



✔️ Notes

\- This is the optimal O(n) solution.

\- A naive solution would recompute heights repeatedly, resulting in O(n²) time — your solution avoids this.

\- Perfect for practicing DFS and tree height calculations.

