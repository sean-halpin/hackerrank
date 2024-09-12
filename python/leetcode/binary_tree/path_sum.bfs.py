# leetcode url: https://leetcode.com/problems/path-sum/

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # return dfs(root, 0, targetSum)
        if root:
            q = deque()
            q.append((root, root.val))

            while q:
                curr, acc = q.popleft()
                if not curr.left and not curr.right and (acc == targetSum):
                    return True
                if curr.left:
                    q.append((curr.left, curr.left.val + acc))
                if curr.right:
                    q.append((curr.right, curr.right.val + acc))
        return False
            