from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            tmp = nums[:i] + nums[i+1:]
            product = reduce(lambda x,y: x*y, tmp)
            result.append(product)
        return result
