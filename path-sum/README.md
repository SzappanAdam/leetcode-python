Path Sum — Python Solution

📌 Problem Description

Given the root of a binary tree and an integer targetSum, determine whether the tree has a root‑to‑leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Examples

\- Input: root = \[5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22

Output: True

\- Input: root = \[1,2,3], targetSum = 5

Output: False

\- Input: root = \[], targetSum = 0

Output: False



💡 Approach

The solution uses a depth‑first search (DFS) to explore all root‑to‑leaf paths.

Key idea:

\- At each node, subtract the node’s value from targetSum

\- When reaching a leaf, check whether the remaining sum equals the leaf’s value

\- If any path returns True, the whole function returns True

This ensures that only complete root‑to‑leaf paths are considered valid.



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



def hasPathSum(root: TreeNode, targetSum: int) -> bool:

&nbsp;   """

&nbsp;   Determines whether the binary tree has a root-to-leaf path

&nbsp;   whose values sum to targetSum.

&nbsp;   """

&nbsp;   if not root:

&nbsp;       return False



&nbsp;   # If it's a leaf, check if the remaining sum matches the node's value

&nbsp;   if not root.left and not root.right:

&nbsp;       return targetSum == root.val



&nbsp;   # Continue searching in the subtrees

&nbsp;   targetSum -= root.val

&nbsp;   return (

&nbsp;       hasPathSum(root.left, targetSum) or

&nbsp;       hasPathSum(root.right, targetSum)

&nbsp;   )



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



root = build\_tree(\[5,4,8,11,None,13,4,7,2,None,None,None,1])

print(hasPathSum(root, 22))  # True



📁 File Structure

path-sum/

│

├── has\_path\_sum.py   # Python implementation

└── README.md         # Documentation



✔️ Notes

\- This is the standard DFS solution.

\- The key detail is checking the sum only at leaf nodes.

\- Perfect for practicing recursion and root‑to‑leaf path logic.

