from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: Optional[TreeNode]) -> str:
    if not root:
        return "n"  # Return 'n' for null/None trees
    
    queue = deque([root])
    output = ""
    
    while queue:
        node = queue.popleft()
        if node is None:
            output += "n"  # Append 'n' for None nodes
        else:
            output += str(node.val)  # Append the node's value
            queue.append(node.left)  # Enqueue left child
            queue.append(node.right) # Enqueue right child
            
    return output

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_1 = bfs(p)
        res_2 = bfs(q)
        print(res_1)
        print(res_2)
        return res_1 == res_2
