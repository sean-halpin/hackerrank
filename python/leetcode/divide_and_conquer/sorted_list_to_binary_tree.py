# leetcode url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# leetcode difficulty: easy
# leetcode problem: 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryBuild(self, nums, begin, end):
        mid = begin + ((end - begin) // 2)
        print(mid)
        n = TreeNode(nums[mid])
        if (end - begin) >= 0:
            n.left = self.binaryBuild(nums, begin, mid -1)
            n.right = self.binaryBuild(nums, mid + 1, end)
        else: 
            return None
        return n

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.binaryBuild(nums, 0, len(nums)-1)