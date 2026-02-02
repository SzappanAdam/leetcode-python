Binary Tree Inorder Traversal — Python Solution

📌 Problem Description

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal follows the pattern:

\\mathrm{Left\\  Subtree}\\rightarrow \\mathrm{Root}\\rightarrow \\mathrm{Right\\  Subtree}

This is one of the fundamental depth‑first traversal methods for binary trees.

Examples

\- Input: \[1, None, 2, 3]

Output: \[1, 3, 2]

\- Input: \[]

Output: \[]

\- Input: \[1]

Output: \[1]



💡 Approach

The solution uses a recursive inorder traversal:

\- Traverse the left subtree

\- Visit the current node

\- Traverse the right subtree

This approach naturally follows the definition of inorder traversal and is easy to implement.



🧠 Time \& Space Complexity

\- Time Complexity: O(n)

Every node is visited exactly once.

\- Space Complexity:

\- O(h) recursion stack, where h is the tree height

\- Worst case (skewed tree): O(n)

\- Best case (balanced tree): O(log n)



📝 Code Implementation

class TreeNode:

&nbsp;   def \_\_init\_\_(self, val=0, left=None, right=None):

&nbsp;       self.val = val

&nbsp;       self.left = left

&nbsp;       self.right = right



def inorderTraversal(root: TreeNode) -> list\[int]:

&nbsp;   """

&nbsp;   Returns the inorder traversal of a binary tree.

&nbsp;   Uses a simple recursive DFS approach.

&nbsp;   """

&nbsp;   res = \[]



&nbsp;   def inorder(node):

&nbsp;       if not node:

&nbsp;           return

&nbsp;       inorder(node.left)

&nbsp;       res.append(node.val)

&nbsp;       inorder(node.right)



&nbsp;   inorder(root)

&nbsp;   return res



🧪 Example Usage

Since LeetCode uses a TreeNode structure, here is a helper to build a tree from a list:

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



root = build\_tree(\[1, None, 2, 3])

print(inorderTraversal(root))  # \[1, 3, 2]



📁 File Structure

binary-tree-inorder-traversal/

│

├── inorder\_traversal.py   # Python implementation

└── README.md              # Documentation



✔️ Notes

\- This is the classic recursive solution.

\- An iterative stack‑based version also exists, but recursion is cleaner and equally efficient.

\- Perfect for practicing tree traversal fundamentals.

