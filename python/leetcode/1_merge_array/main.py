from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = [0] * (m + n)
        j, k = 0, 0
        for i in range(m + n):
            if j < m and (k >= n or nums1[j] < nums2[k]):
                temp[i] = nums1[j]
                j += 1
            else:
                temp[i] = nums2[k]
                k += 1
        nums1[:] = temp

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)