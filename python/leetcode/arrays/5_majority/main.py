from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        maj = 0
        maj_count = 0
        for n in nums:
            if n in occ:
                occ[n] = occ[n] + 1
            else:
                occ[n] = 1
            if occ[n] > maj_count:
                maj = n
                maj_count = occ[n]
        return maj
    
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2] 
    solution = Solution() 
    result = solution.majorityElement(nums) 
    print(result)