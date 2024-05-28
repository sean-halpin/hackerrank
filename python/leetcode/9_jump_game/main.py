from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = 1
        for i in range(len(nums)):
            dist -= 1
            if nums[i] > dist:
                dist = nums[i]
            if dist == 0 and i != (len(nums) -1):
                return False
        return True
            
if __name__ == "__main__": 
    sol = Solution()
    arr = [3,2,1,0,4]
    res = sol.canJump(arr)
    print(res)
    assert res == False
    
    arr_b = [2,3,1,1,4]
    res = sol.canJump(arr_b)
    print(res)
    assert res == True
    