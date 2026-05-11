# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        def dfs(row,col):
            if grid[row][col] == 0:
                return 0
            count = 1
            grid[row][col] = 0
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in directions:
                if 0<= row+dx < len(grid) and 0 <= col+dy < len(grid[0]):
                    count += dfs(row+dx,col+dy)
            return count
            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    result = max(result,dfs(i,j))
        return result