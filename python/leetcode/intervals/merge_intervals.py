# leetcode: https://leetcode.com/problems/merge-intervals/
# 

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1]) # merge overlap
            else:
                result.append(prev)
                prev = intervals[i]
        result.append(prev)
        return result