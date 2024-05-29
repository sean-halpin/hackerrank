class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        l = 0
        r = n - 1
        for i in range(len(numbers)):
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
        return [-1,-1]




if __name__ == "__main__":
    sol = Solution()
    numbers = [2,7,11,15]
    target = 9
    result = sol.twoSum(numbers, target)
    print(result)
    assert result == [1,2]