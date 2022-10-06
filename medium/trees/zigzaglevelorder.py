# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zig = True
        ans = []
        level_count = 0
        next_level_count = 0
        dq = deque()

        if root:
            dq.append(root)
            level_count = 1

        temp = []
        while dq:
            curr = None
            if zig:
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                    next_level_count += 1
                if curr.right:
                    next_level_count += 1
                    dq.append(curr.right)
            else:
                curr = dq.pop()
                if curr.left:
                    dq.appendleft(curr.right)
                    next_level_count += 1
                if curr.right:
                    next_level_count += 1
                    dq.appendleft(curr.left)
            level_count -= 1
            temp.append(curr.val)
            if level_count == 0:
                ans.append(temp)
                temp = []
                zig = not zig
                level_count = next_level_count
                next_level_count = 0
        return ans
