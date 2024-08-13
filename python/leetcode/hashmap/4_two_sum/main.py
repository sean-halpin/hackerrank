from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if n not in seen:
                seen[n] = i
            if target - n in seen and seen[target - n] is not i:
                return [seen[target - n], i]
        return [-1,-1]
    
if __name__ == "__main__":
    sol = Solution()
    numbers = [2,7,11,15]
    target = 9
    result = sol.twoSum(numbers, target)
    print(result)
    assert result == [0,1]