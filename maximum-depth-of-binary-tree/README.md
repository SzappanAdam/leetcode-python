Maximum Depth of Binary Tree — Python Solution

📌 Problem Description

Given the root of a binary tree, return its maximum depth.

The maximum depth is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Examples

\- Input: \[3,9,20,None,None,15,7]

Output: 3

\- Input: \[]

Output: 0

\- Input: \[1]

Output: 1



💡 Approach

The solution uses a recursive depth‑first search (DFS).

For any node:

\\mathrm{depth}(node)=1+\\max (\\mathrm{depth(left)},\\mathrm{depth(right)})

Steps:

\- If the node is None, return 0

\- Recursively compute the depth of the left subtree

\- Recursively compute the depth of the right subtree

\- Return the larger of the two depths + 1

This approach naturally follows the structure of the tree.



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



def maxDepth(root: TreeNode) -> int:

&nbsp;   """

&nbsp;   Returns the maximum depth of a binary tree.

&nbsp;   Uses a recursive DFS approach.

&nbsp;   """

&nbsp;   if not root:

&nbsp;       return 0

&nbsp;   left\_depth = maxDepth(root.left)

&nbsp;   right\_depth = maxDepth(root.right)

&nbsp;   return max(left\_depth, right\_depth) + 1



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

print(maxDepth(root))  # 3



📁 File Structure

maximum-depth-of-binary-tree/

│

├── max\_depth.py   # Python implementation

└── README.md      # Documentation



✔️ Notes

\- This is the standard recursive DFS solution.

\- An iterative BFS version also exists, but recursion is clean and intuitive.

\- Perfect for practicing tree traversal and recursion fundamentals.

