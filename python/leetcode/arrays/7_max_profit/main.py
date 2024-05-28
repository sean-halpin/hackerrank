from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_int = sys.maxsize
        best_max = 0
        best_min = max_int
        poss_max = 0 
        poss_min = max_int
        
        for price in prices:
            if price > poss_max:
                poss_max = price
            if price < poss_min:
                poss_max = price
                poss_min = price
            if poss_max - poss_min > best_max - best_min:
                best_max = poss_max
                best_min = poss_min
        return (best_max - best_min) if (best_max != 0) else 0 
          
if __name__ == '__main__':
    sol = Solution()
    prices = [1,2,3,4,5,6]
    r = sol.maxProfit(prices)
    print(r)