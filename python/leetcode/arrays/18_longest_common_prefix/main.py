from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0]
        max = 0
        smallest_string = min(strs, key=lambda s: (len(s), s))
        for i in range(len(smallest_string)):
            matched = [m[i] for m in strs if m[i] == smallest_string[i]]
            # print(matched)
            if len(matched) == len(strs):
                max += 1
            else:
                break
        return strs[0][:max]
    
if __name__ == "__main__":
    solution = Solution()
    # Test case 1: Longest common prefix is "fl"
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    # Test case 2: Longest common prefix is ""
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    # Test case 3: Longest common prefix is "a"
    assert solution.longestCommonPrefix(["a"]) == "a"
    # Test case 4: Longest common prefix is ""
    assert solution.longestCommonPrefix(["", ""]) == ""
    # Test case 5: Longest common prefix is ""
    assert solution.longestCommonPrefix([""]) == ""
    # Test case 6: Longest common prefix is "a"
    assert solution.longestCommonPrefix(["a", "a"]) == "a"
    # Test case 7: Longest common prefix is "a"
    assert solution.longestCommonPrefix(["a", "a", "a"]) == "a"