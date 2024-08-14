# leetcode url: https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, n in enumerate(nums):
            if n in seen:
                if abs(seen[n] - i) <= k:
                    print(seen, i, n, k)
                    return True
            seen[n] = i
        return False

