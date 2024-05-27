from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for p in prices[1:]:
            if p < min:
                min = p
            if p - min > 0:
                profit += (p - min)
                min = p
        return profit
    
if __name__ == "__main__":
    sol = Solution()
    arr = [7,1,5,3,6,4]
    result = sol.maxProfit(arr)
    print(result)
    assert result == 7