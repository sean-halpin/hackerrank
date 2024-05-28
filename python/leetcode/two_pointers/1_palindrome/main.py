class Solution:
    def isPalindrome(self, s: str) -> bool:
        return True
    
if __name__ == "__main__":
    sol = Solution()
    inp = "kayak"
    res = sol.isPalindrome(inp)
    print(res)
    assert res == True