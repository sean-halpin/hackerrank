class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = [word for word in s.split(" ") if word.isalpha()]
        return len(split[len(split) - 1])
    
# Test case 1: Last word has length 5
solution = Solution()
assert solution.lengthOfLastWord("Hello World") == 5

# Test case 2: Last word has length 3
solution = Solution()
assert solution.lengthOfLastWord("This is a test") == 4