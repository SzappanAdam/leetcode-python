class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    """
    Determines whether the binary tree has a root-to-leaf path
    whose values sum to targetSum.
    """
    if not root:
        return False

    # If it's a leaf, check if the remaining sum matches the node's value
    if not root.left and not root.right:
        return targetSum == root.val

    # Continue searching in the subtrees
    targetSum -= root.val
    return (
        hasPathSum(root.left, targetSum) or
        hasPathSum(root.right, targetSum)
    )