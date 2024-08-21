# leetcode url: https://leetcode.com/problems/palindrome-number/
# leetcode problem: 9. Palindrome Number
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    assert sol.isPalindrome(121) == True

    # Example 2
    assert sol.isPalindrome(-121) == False

    # Example 3
    assert sol.isPalindrome(10) == False

    # Example 4
    assert sol.isPalindrome(-101) == False

    print("All examples are correct")

# Algorithm used: Convert to string
# Time complexity: O(n)
# Space complexity: O(n)