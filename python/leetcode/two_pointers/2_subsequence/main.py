class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        for c in s:
            if c not in t[i:]:
                return False
            else: 
                i = i + t[i:].index(c) + 1
        return True

if __name__ == "__main__": 
    sol = Solution()
    result = sol.isSubsequence("abc", "asdfsbfsdfsc")
    print(result)
    assert result == True