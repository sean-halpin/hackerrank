# leetcode url : https://leetcode.com/problems/invert-binary-tree/

from collections import deque
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
        # dfs_flip(root)
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
        return root