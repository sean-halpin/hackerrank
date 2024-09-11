# leetcode url: https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        lidx = 0
        lhmax = 0
        ridx = len(height)-1
        rhmax = 0

        rain = 0
        while lidx <= ridx:
            print(lidx, ridx)
            lhmax = max(lhmax, height[lidx])
            rhmax = max(rhmax, height[ridx])

            if lhmax > rhmax:
                rain += min(lhmax, rhmax) - height[ridx]
                ridx -= 1
            else:
                rain += min(lhmax, rhmax) - height[lidx]
                lidx += 1

        return rain
