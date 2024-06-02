from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        bottom = len(matrix)
        top = 0
        dir = 0
        visited = []
        while len(visited) < len(matrix[0]) * len(matrix):
            if dir == 0:
                for x in range(left, right):
                    visited.append(matrix[top][x])
                top+=1
            if dir == 1:
                for y in range(top,bottom):
                    visited.append(matrix[y][right-1])
                right-=1
            if dir == 2:
                for x in range(right, left, -1):
                    visited.append(matrix[bottom-1][x-1])
                bottom-=1
            if dir == 3:
                for y in range(bottom,top, -1):
                    visited.append(matrix[y-1][left])
                left+=1
            dir = (dir + 1) % 4
        return visited

if __name__ == "__main__":
    sol = Solution()
    inp = [[1,2,3],[4,5,6],[7,8,9]]
    res = sol.spiralOrder(inp)
    print(res)
    assert res == [1,2,3,6,9,8,7,4,5]