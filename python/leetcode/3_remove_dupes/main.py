from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = set(nums)
        nums[:] = list(uniq)
        nums.sort()
        return len(nums)
    
if __name__ == '__main__':
    nums = [1,1,2]
    sol = Solution()
    print(sol.removeDuplicates(nums))
    print(nums)