# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

 

# Example 1:



# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.

from typing import List
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        rows,cols = len(isWater),len(isWater[0])
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]==1:
                    isWater[i][j] = 0
                    queue.append((i,j))
                else:
                    isWater[i][j] = -1 # not visited
        directions = [(1,0),(0,-1),(-1,0),(0,1)]
        while queue:
            r,c = queue.popleft()
            for dx,dy in directions:
                nx,ny = dx+r,dy+c
                if 0<=nx<rows and 0<=ny<cols and (isWater[nx][ny] == -1 ):
                    isWater[nx][ny] = isWater[r][c] + 1
                    queue.append((nx,ny))
        return isWater
            
            
