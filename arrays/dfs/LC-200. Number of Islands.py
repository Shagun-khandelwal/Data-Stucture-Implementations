# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(row,col):
            if grid[row][col] == "0":
                return
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            grid[row][col]="0"
            for dx,dy in directions:
                if 0 <= row + dx < len(grid) and 0 <= col+dy < len(grid[0]):
                    dfs(row+dx,col+dy)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)
        return count