# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N,n = 9,3
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9
        isSolved = False

        # rows = [[0]*(N+1) for _ in range(N)]
        # cols = [[0]*(N+1) for _ in range(N)]
        # boxes = [[0]*(N+1) for _ in range(N)]
        def getBoxId(r,c):
            return (r//n)*n + c//n

        def canPlace(num,r,c):
            box_idx = getBoxId(r,c)
            mask = 1<<num
            return not (rows[r] & mask or cols[c] & mask or boxes[box_idx] & mask)

        def placeNextNumber(r,c):
            nonlocal isSolved
            if r == N-1 and c == N-1:
                isSolved = True
            elif c == N-1:
                fillSudoku(r+1,0)
            else:
                fillSudoku(r,c+1)

        def removeNumber(digit,i,j):
            box_idx = getBoxId(i,j)
            mask = 1<<digit
            rows[i] ^= mask
            cols[j] ^= mask
            boxes[box_idx] ^= mask
            board[i][j]="."
        
        def placeNumber(digit,i,j):
            box_idx = getBoxId(i,j)
            mask = 1<<digit
            rows[i] |= mask
            cols[j] |= mask
            boxes[box_idx] |= mask
            board[i][j] = str(digit)
        
        
        def fillSudoku(i,j):
            if board[i][j] == ".":
                for num in range(1,10):
                    if canPlace(num,i,j):
                        placeNumber(num,i,j)
                        placeNextNumber(i,j)
                        if not isSolved:
                            removeNumber(num,i,j)
            else:
                placeNextNumber(i,j) 

        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    placeNumber(int(board[i][j]),i,j)

        fillSudoku(0,0)