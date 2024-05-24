from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [elem for elem in nums if elem != val]
        return len(nums)
    
if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    sol = Solution()
    print(sol.removeElement(nums, val))
    print(nums)
