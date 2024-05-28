from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        max_c = max(citations)
        if max_c == 0:
            return 0
        res = {}
        for i in range(max_c + 1):
            s = sum(1 for c in citations if c >=i)
            res[i] = s
        print(res)
        return max((k) for (k,v) in res.items() if v >= k) 

if __name__ == "__main__":
    sol = Solution()
    arr = [1,1,2]
    result = sol.hIndex(arr)
    print(result)
    assert result == 1