from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        tmp = []
        for num in nums:
            if num not in seen:
                seen[num] = 1
                tmp.append(num)
            elif seen[num] == 1:
                seen[num] = 2
                tmp.append(num)
        nums[:] = tmp
        
        
if __name__ == '__main__':
    # Create an instance of the Solution class
    solution = Solution()

    # Call the removeDuplicates method with a list of numbers
    nums = [1, 1, 2, 2, 2, 3]
    solution.removeDuplicates(nums)

    # Print the modified list
    print(nums)