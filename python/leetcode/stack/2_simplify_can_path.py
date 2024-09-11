# leetcode url: https://leetcode.com/problems/simplify-path/
# 

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        spl = path.split("/")
        for c in spl:
            if c == "..":
                stack.pop() if len(stack) > 0 else None
            elif c != "" and c != ".":
                stack.append(c)
        
        return "/" + "/".join(stack)