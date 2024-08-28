# leetcode problem: 100. Same Tree
# leetcode url: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(n: Optional[TreeNode], outp: str = ""):
    if n is None:
        return outp + "n"
    outp += str(n.val)
    outp += dfs(n.left)
    outp += dfs(n.right)
    return outp
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_1 = dfs(p)
        res_2 = dfs(q)
        print(res_1)
        print(res_2)
        return res_1 == res_2
    
if __name__ == "__main__": 
    # Example 1
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    assert Solution().isSameTree(p, q) == True

    # Example 2
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    assert Solution().isSameTree(p, q) == False

    # Example 3
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    assert Solution().isSameTree(p, q) == False

    print("All examples are correct")