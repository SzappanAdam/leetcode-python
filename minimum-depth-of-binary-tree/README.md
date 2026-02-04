Minimum Depth of Binary Tree — Python Solution

📌 Problem Description

Given the root of a binary tree, return its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

A leaf is a node with no children.

Examples

\- Input: \[3,9,20,None,None,15,7]

Output: 2

\- Input: \[2,None,3,None,4,None,5,None,6]

Output: 5

\- Input: \[]

Output: 0



💡 Approach

A common mistake is to take:

\\min (\\mathrm{left},\\mathrm{right})+1

But this is incorrect when one subtree is missing, because the missing side has depth 0, which would incorrectly dominate the minimum.

Your solution handles this perfectly by treating missing children as special cases.

Steps:

\- If the node is None, return 0

\- If the left child is missing, return the depth of the right subtree + 1

\- If the right child is missing, return the depth of the left subtree + 1

\- Otherwise, return the minimum of the two subtree depths + 1

This ensures the minimum depth always reaches a real leaf.



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



def minDepth(root: TreeNode) -> int:

&nbsp;   """

&nbsp;   Returns the minimum depth of a binary tree.

&nbsp;   Correctly handles cases where one subtree is missing.

&nbsp;   """

&nbsp;   if not root:

&nbsp;       return 0



&nbsp;   if not root.left:

&nbsp;       return minDepth(root.right) + 1

&nbsp;   if not root.right:

&nbsp;       return minDepth(root.left) + 1



&nbsp;   return min(minDepth(root.left), minDepth(root.right)) + 1



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

print(minDepth(root))  # 2



📁 File Structure

minimum-depth-of-binary-tree/

│

├── min\_depth.py   # Python implementation

└── README.md      # Documentation



✔️ Notes

\- This solution avoids the classic pitfall of incorrectly using min() when one subtree is missing.

\- The logic is clean, optimal, and matches the official editorial.

\- Perfect for practicing recursion and understanding leaf‑based depth calculations.

