# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def dfs(row,col):
            if row < 0 or row >= rows or col <0 or col >= cols or board[row][col]!="O": # out of bound
                return
            
            # Mark that border-connected O to safe S
            board[row][col]="S"
            directions = [(1,0),(0,-1),(-1,0),(0,1)]
            for dx,dy in directions:
                dfs(row+dx,col+dy)
        
        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X" # Captured
                elif board[i][j] == "S":
                    board[i][j] = "O" # Safe O's
        
                


            
        