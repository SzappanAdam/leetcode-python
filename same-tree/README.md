Same Tree — Python Solution

📌 Problem Description

Given the roots of two binary trees p and q, determine whether the two trees are identical.

Two binary trees are considered the same if:

\- They have the same structure

\- The corresponding nodes have the same values

Examples

\- Input: p = \[1,2,3], q = \[1,2,3]

Output: True

\- Input: p = \[1,2], q = \[1,None,2]

Output: False

\- Input: p = \[], q = \[]

Output: True



💡 Approach

The solution uses a simple recursive comparison:

\- If both nodes are None, the trees match at this branch

\- If only one is None, the trees differ

\- If the values differ, the trees differ

\- Recursively compare:

\- left subtrees

\- right subtrees

This approach naturally mirrors the structure of the trees.



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



def isSameTree(p: TreeNode, q: TreeNode) -> bool:

&nbsp;   """

&nbsp;   Determines whether two binary trees are identical.

&nbsp;   Compares structure and node values recursively.

&nbsp;   """

&nbsp;   if not p and not q:

&nbsp;       return True

&nbsp;   if not p or not q:

&nbsp;       return False

&nbsp;   if p.val != q.val:

&nbsp;       return False

&nbsp;   return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)



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



p = build\_tree(\[1,2,3])

q = build\_tree(\[1,2,3])

print(isSameTree(p, q))  # True



📁 File Structure

same-tree/

│

├── is\_same\_tree.py   # Python implementation

└── README.md         # Documentation



✔️ Notes

\- This is the standard recursive solution.

\- An iterative version using a queue or stack also exists, but recursion is cleaner.

\- Perfect for practicing tree comparison and recursion fundamentals.

