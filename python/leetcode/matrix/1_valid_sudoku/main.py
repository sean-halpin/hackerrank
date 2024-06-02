class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # rows
        for i in range(len(board[0])):
            col = [row[i] for row in board]
            numerics = [num for num in col if num.isnumeric()]
            uniq = set(numerics)
            if len(numerics) != len(uniq):
                return False
        for row in board:
            numerics = [num for num in row if num.isnumeric()]
            uniq = set(numerics)
            if len(numerics) != len(uniq):
                return False
        for x in range(0,9,3):
            for y in range(0,9,3):
                tbyt = []
                for xx in range(0,3,1):
                    for yy in range(0,3,1):
                        tbyt.append(board[x+xx][y+yy])
                numerics = [num for num in tbyt if num.isnumeric()]
                uniq = set(numerics)
                if len(numerics) != len(uniq):
                    return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    result = sol.isValidSudoku(board)
    print(result)
    assert result == False