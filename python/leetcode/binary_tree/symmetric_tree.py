# leetcode: https://leetcode.com/problems/symmetric-tree/
# tags: binary tree, dfs

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def symCheck(self, n1, n2):
        if n1 and n2:
            # print(n1.val, n2.val)
            if n1.val != n2.val:
                return False
            elif n1.val == n2.val and self.symCheck(n1.left, n2.right) and self.symCheck(n1.right, n2.left):
                return True
        elif not n1 and not n2:
            return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symCheck(root.left, root.right)
