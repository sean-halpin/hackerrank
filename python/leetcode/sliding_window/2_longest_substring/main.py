class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        l = 0
        longest = 0
        for r in range(1,n+1):
            substr = s[l:r]
            # print(l,r,substr)
            if len(set(substr)) == r-l:
                if r-l > longest:
                    longest = r-l
            else:
                l = l+1
        return longest
            
if __name__ == "__main__": 
    sol = Solution()
    inp = "abdvdakja"
    res = sol.lengthOfLongestSubstring(inp)
    print(res)
    assert res == 5
        