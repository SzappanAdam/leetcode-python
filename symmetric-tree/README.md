Symmetric Tree — Python Solution

📌 Problem Description

Given the root of a binary tree, determine whether the tree is symmetric around its center.

A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Examples

\- Input: \[1,2,2,3,4,4,3]

Output: True

\- Input: \[1,2,2,None,3,None,3]

Output: False

\- Input: \[]

Output: True



💡 Approach

The solution uses a recursive mirror check.

Two trees are mirror images if:

\- Their root values are equal

\- The left subtree of one is a mirror of the right subtree of the other

\- The right subtree of one is a mirror of the left subtree of the other

This leads to a clean recursive function isMirror(t1, t2).



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



def isSymmetric(root: TreeNode) -> bool:

&nbsp;   """

&nbsp;   Determines whether a binary tree is symmetric around its center.

&nbsp;   Uses a recursive mirror comparison.

&nbsp;   """

&nbsp;   if not root:

&nbsp;       return True



&nbsp;   def isMirror(t1, t2):

&nbsp;       if not t1 and not t2:

&nbsp;           return True

&nbsp;       if not t1 or not t2:

&nbsp;           return False

&nbsp;       return (

&nbsp;           t1.val == t2.val and

&nbsp;           isMirror(t1.left, t2.right) and

&nbsp;           isMirror(t1.right, t2.left)

&nbsp;       )



&nbsp;   return isMirror(root.left, root.right)



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



root = build\_tree(\[1,2,2,3,4,4,3])

print(isSymmetric(root))  # True



📁 File Structure

symmetric-tree/

│

├── is\_symmetric.py   # Python implementation

└── README.md         # Documentation



✔️ Notes

\- This is the standard recursive solution.

\- An iterative version using a queue also exists, but recursion is cleaner and intuitive.

\- Perfect for practicing tree symmetry and recursive thinking.

