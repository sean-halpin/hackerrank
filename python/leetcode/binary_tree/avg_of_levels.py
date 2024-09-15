# leetcode url: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, levels, counts, lvl):
    if node:
        levels[lvl] += node.val  # Accumulate the sum of values at this level
        counts[lvl] += 1         # Count the number of nodes at this level
        
        dfs(node.left, levels, counts, lvl + 1)
        dfs(node.right, levels, counts, lvl + 1)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = defaultdict(int)   # Store the sum of node values per level
        counts = defaultdict(int)   # Store the count of nodes per level
        dfs(root, levels, counts, 0)
        
        # Calculate the average for each level
        return [levels[i] / counts[i] for i in range(len(levels))]