# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

# Example 1:


# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
# Example 2:


# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
#  time complexity: O(m*n)
# space complexity: O(m*n) in worst case when all cells are land cells
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #  we run over the boundaries and make adjacent land cells(1s) to -1 using depth first search

        def dfs(row,col):
            if grid[row][col] != 1:
                return
            grid[row][col] = -1 #visited
            directions = [(1,0),(0,-1),(-1,0),(0,1)]

            for dx,dy in directions:
                nx,ny = dx+row,dy+col
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                    dfs(nx,ny)
            


        rows,cols = len(grid),len(grid[0])

        for i in range(rows): # 0th column and last column
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][cols-1] == 1:
                dfs(i,cols-1)
        
        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[rows-1][j] == 1:
                dfs(rows-1,j)
        print(grid)
        move = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    move+=1
        return move