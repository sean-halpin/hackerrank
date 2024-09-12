# leetcode url: https://leetcode.com/problems/path-sum/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, currSum, targetSum) -> bool:
    if node:
        if node.val + currSum == targetSum and not node.left and not node.right:
            return True
        else:
            left_found = dfs(node.left, node.val + currSum, targetSum)
            right_found = dfs(node.right, node.val + currSum, targetSum)
            return left_found or right_found
    else:
        return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return dfs(root, 0, targetSum)