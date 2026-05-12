# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

 

# Example 1:



# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
# Example 2:



# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0
        def dfs(row,col):
            if row <0 or row >= len(grid) or col <0 or col >= len(grid[0]):
                return False

            if grid[row][col] == 1:
                return True
            
            
            directions = [(1,0),(0,-1),(-1,0),(0,1)] # right,bottom,left,top
            isClosed = True
            grid[row][col] =  1 # visited
            for dx,dy in directions:
                nx,ny = dx+row,dy+col
                temp = dfs(nx,ny)
                isClosed =  isClosed and temp
            return isClosed

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    result += 1 if dfs(i,j) else 0
        return result