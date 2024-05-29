import sys

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        curr_sum = 0
        minimum = sys.maxsize

        for r in range(n):
            curr_sum += nums[r]
            while curr_sum >= target:
                minimum = min(minimum, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if minimum == sys.maxsize else minimum

if __name__ == "__main__":
    sol = Solution()
    inp = [2,3,10,5,7,8,9]
    result = sol.minSubArrayLen(13, inp)
    print(result)
    assert result == 2