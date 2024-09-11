# leetcode url: https://leetcode.com/problems/binary-tree-right-side-view/
# 

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, level, lvl_visited, rsv):
    if node:
        if level not in lvl_visited:
            lvl_visited.add(level)
            rsv.append(node.val)
        if node.right:
            dfs(node.right, level + 1, lvl_visited, rsv)
        if node.left:
            dfs(node.left, level + 1, lvl_visited, rsv)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rsv = [] # rsv nodes
        visited = set() # levels visited
        dfs(root, 0, visited, rsv)
        return rsv