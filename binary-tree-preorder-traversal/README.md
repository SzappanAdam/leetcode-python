Binary Tree Preorder Traversal — Python Solution

📌 Problem Description

Given the root of a binary tree, return the preorder traversal of its nodes’ values.

Preorder traversal visits nodes in the following order:

\- Root

\- Left subtree

\- Right subtree

Examples

\- Input: \[1, None, 2, 3]

Output: \[1, 2, 3]

\- Input: \[]

Output: \[]

\- Input: \[1]

Output: \[1]



💡 Approach

This solution uses a simple depth‑first search (DFS) with recursion.

At each node:

\- Visit the node (append its value)

\- Traverse the left subtree

\- Traverse the right subtree

This directly follows the preorder definition.



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



def preorderTraversal(root: TreeNode):

&nbsp;   """

&nbsp;   Returns the preorder traversal of a binary tree.

&nbsp;   Order: root -> left -> right

&nbsp;   """

&nbsp;   result = \[]



&nbsp;   def dfs(node):

&nbsp;       if not node:

&nbsp;           return

&nbsp;       result.append(node.val)   # Visit root

&nbsp;       dfs(node.left)            # Traverse left

&nbsp;       dfs(node.right)           # Traverse right



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



print(preorderTraversal(root))  # \[1, 2, 3]



📁 File Structure

binary-tree-preorder-traversal/

│

├── preorder\_traversal.py   # Python implementation

└── README.md               # Documentation



✔️ Notes

\- This is the classic recursive preorder traversal.

\- The logic is clean, minimal, and matches the official editorial.

\- Great foundational problem for understanding DFS on trees.

