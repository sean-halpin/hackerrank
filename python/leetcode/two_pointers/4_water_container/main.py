class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_vol = 0
        l = 0
        r = n - 1
        for i in range(n):
            m = min(height[l], height[r]) * ((r)-(l))
            max_vol = max(m, max_vol)
            print(l,r)
            print(max_vol)
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
            if l>r:
                break
        return max_vol

if __name__ == "__main__":
    sol = Solution()
    inp = [2,3,10,5,7,8,9]
    result = sol.maxArea(inp)
    print(result)
    assert result == 36