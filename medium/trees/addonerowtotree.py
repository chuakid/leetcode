# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if depth == 1:
            newNode = TreeNode(val, root, None)
            return newNode
        if depth == 2:
            newLeftNode = TreeNode(val, root.left, None)
            newRightNode = TreeNode(val, None, root.right)
            root.left = newLeftNode
            root.right = newRightNode
            return root
        self.addOneRow(root.left, val, depth - 1)
        self.addOneRow(root.right, val, depth - 1)
        return root
