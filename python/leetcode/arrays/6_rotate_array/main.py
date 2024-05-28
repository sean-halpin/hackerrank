from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        shift = k % length
        split = (length-shift)
        l = nums[:split]
        r = nums[split:]
        nums[:] = r + l
        
        
if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,3,4,5]
    sol.rotate(arr, 1)
    print(arr)