class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_size = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+window_size] == needle:
                return i
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    # Test case 1: Needle "ll" is found in haystack "hello" at index 2
    assert solution.strStr("hello", "ll") == 2
    # Test case 2: Needle "bba" is not found in haystack "aaaaa"
    assert solution.strStr("aaaaa", "bba") == -1
    # Test case 3: Needle "" is found in haystack "" at index 0
    assert solution.strStr("", "") == -1
    # Test case 4: Needle "a" is found in haystack "a" at index 0
    assert solution.strStr("a", "a") == 0
    # Test case 5: Needle "a" is not found in haystack "b" at index -1
    assert solution.strStr("b", "a") == -1
    # Test case 6: Needle "a" is found in haystack "ab" at index 0
    assert solution.strStr("ab", "a") == 0
    # Test case 7: Needle "a" is found in haystack "ba" at index 1
    assert solution.strStr("ba", "a") == 1
    # Test case 8: Needle "a" is found in haystack "baa" at index 1
    assert solution.strStr("baa", "a") == 1