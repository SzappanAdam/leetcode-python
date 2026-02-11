Binary Tree Postorder Traversal — Python Solution

📌 Problem Description

Given the root of a binary tree, return the postorder traversal of its nodes’ values.

Postorder traversal visits nodes in the following order:

\- Left subtree

\- Right subtree

\- Root

Examples

\- Input: \[1, None, 2, 3]

Output: \[3, 2, 1]

\- Input: \[]

Output: \[]

\- Input: \[1]

Output: \[1]



💡 Approach

This solution uses a simple depth‑first search (DFS) with recursion.

At each node:

\- Traverse the left subtree

\- Traverse the right subtree

\- Visit the node (append its value)

This directly follows the postorder definition.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Each node is visited exactly once.

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



def postorderTraversal(root: TreeNode):

&nbsp;   """

&nbsp;   Returns the postorder traversal of a binary tree.

&nbsp;   Order: left -> right -> root

&nbsp;   """

&nbsp;   result = \[]



&nbsp;   def dfs(node):

&nbsp;       if not node:

&nbsp;           return

&nbsp;       dfs(node.left)       # Traverse left

&nbsp;       dfs(node.right)      # Traverse right

&nbsp;       result.append(node.val)  # Visit root



&nbsp;   dfs(root)

&nbsp;   return result



🧪 Example Usage

\# Example tree:

\#     1

\#      \\

\#       2

\#      /

\#     3



root = TreeNode(1)

root.right = TreeNode(2)

root.right.left = TreeNode(3)



print(postorderTraversal(root))  # \[3, 2, 1]



📁 File Structure

binary-tree-postorder-traversal/

│

├── postorder\_traversal.py   # Python implementation

└── README.md                # Documentation



✔️ Notes

\- This is the classic recursive postorder traversal.

\- The logic is clean, minimal, and matches the official editorial.

\- Great foundational problem for understanding DFS on trees.

