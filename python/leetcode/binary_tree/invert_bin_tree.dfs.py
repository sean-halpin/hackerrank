# leetcode url: https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_flip(node):
    if node:
        if node.left:
            dfs_flip(node.left)
        if node.right:
            dfs_flip(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs_flip(root)
        return root