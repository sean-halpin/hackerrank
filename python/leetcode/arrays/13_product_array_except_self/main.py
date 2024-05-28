from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        postfix = [1]
        for i in range(1,n):
            prefix.append(nums[i-1] * prefix[i-1])
            postfix.insert(0,nums[n-i] * postfix[0])
        print(prefix, postfix)
        return [x * y for x, y in zip(prefix, postfix)]

if __name__ == "__main__":   
    nums = [1, 2, 3, 4]
    solution = Solution()
    output = solution.productExceptSelf(nums)
    print(output)
    assert output == [24,12,8,6]
