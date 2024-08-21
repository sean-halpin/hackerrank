# leetcode url: https://leetcode.com/problems/plus-one/
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ptr = len(digits) - 1 
        digits[ptr] = (digits[ptr] + 1) % 10
        
        while(digits[ptr] == 0):
            if ptr == 0:
                digits.insert(0, 1)
                break
            ptr = ptr - 1
            digits[ptr] = (digits[ptr] + 1) % 10
            
        return digits
    
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
    
    # Example 2
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    
    # Example 3
    assert sol.plusOne([0]) == [1]
    
    # Example 4
    print(sol.plusOne([9]))
    assert sol.plusOne([9]) == [1, 0]
    
    print("All examples are correct")

