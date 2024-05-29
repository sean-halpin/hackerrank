class Solution:
    def isPalindrome(self, s: str) -> bool:
        upper = s.upper().replace(" ", "")
        cleaned = ''.join([c for c in upper if c.isalnum()])
        i = 0
        j = len(cleaned)-1
        for l in range(j):
            if cleaned[i] == cleaned[j]:
                i += 1
                j -= 1
                if i > j:
                    return True
            else:
                return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    inp = "kayak"
    res = sol.isPalindrome(inp)
    print(res)
    assert res == True