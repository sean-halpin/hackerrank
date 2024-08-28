# leetcode problem: 20. Valid Parentheses
# leetcode url: https://leetcode.com/problems/valid-parentheses/

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()
    
    def empty(self):
        return len(self.stack) == 0

class P:
    pmap = {
            "(":")", 
            "{":"}",
            "[":"]",
            ")":"(",
            "}":"{",
            "]":"["
        }
    def isOpening(c):
        return c in "({["

    def isClosing(c):
        return c in ")}]"

    def isParenth(c):
        return c in "(){}[]"

    def invert(c):
        return P.pmap[c]
    
    def isInverse(c, d):
        return c == P.pmap[d]

class Solution:    
    def isValid(self, s: str) -> bool:
        stack = MyStack()
        chars = list(s)
        for c in chars:
            if P.isParenth(c):
                if P.isOpening(c):
                    stack.push(c)
                if P.isClosing(c):
                    if stack.empty():
                        return False
                    if P.isInverse(c, stack.peek()):
                        stack.pop()
                    else:
                        return False
                
        if stack.empty():
            return True
        else:
            return False
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    assert sol.isValid("()") == True

    # Example 2
    assert sol.isValid("()[]{}") == True

    # Example 3
    assert sol.isValid("(]") == False

    # Example 4
    assert sol.isValid("([)]") == False

    # Example 5
    assert sol.isValid("{[]}") == True
    
    # Example 6
    assert sol.isValid("]") == False

    print("All examples are correct")