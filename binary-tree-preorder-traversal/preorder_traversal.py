class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: TreeNode):
    """
    Returns the preorder traversal of a binary tree.
    Order: root -> left -> right
    """
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)   # Visit root
        dfs(node.left)            # Traverse left
        dfs(node.right)           # Traverse right

    dfs(root)
    return result