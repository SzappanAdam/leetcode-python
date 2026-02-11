class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: TreeNode):
    """
    Returns the postorder traversal of a binary tree.
    Order: left -> right -> root
    """
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)       # Traverse left
        dfs(node.right)      # Traverse right
        result.append(node.val)  # Visit root

    dfs(root)
    return result