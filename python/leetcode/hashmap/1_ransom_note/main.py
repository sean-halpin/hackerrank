from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charCounts = dict()
        for c in ransomNote:
            if c in charCounts:
                charCounts[c] += 1
            else:
                charCounts[c] = 1
        for c in magazine:
            if c in ransomNote:
                charCounts[c] -= 1
        # print("print(charCounts)", charCounts)
        # print(sum([v for k,v in charCounts.items()]))
        return True if all([v<=0 for k,v in charCounts.items()]) else False
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.canConstruct("aa", "aab")
    print(res)
    assert res == True