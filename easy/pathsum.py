# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root is None:
            return False
        x = targetSum - root.val
        # if not leaf
        if root.left is not None or root.right is not None:
            return self.hasPathSum(root.left, x) or self.hasPathSum(root.right, x)
        return x == 0
