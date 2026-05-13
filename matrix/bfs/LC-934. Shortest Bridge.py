# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
 

# Constraints:

# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
# using DFS to find the first island and mark it as 2 and add all the coordinates of that island in the queue and then using BFS to find the shortest distance from that island to the second island. The distance will be the number of 0's we have to flip to connect the two islands.
# time complexity is O(m*n) because we are doing DFS for every cell in the grid and each cell will be visited at most once in each DFS. So the overall time complexity is O(m*n).
# space complexity is O(m*n) because in the worst case, we might have to store all the cells in the visited set for both Pacific and Atlantic oceans. Additionally, the recursion stack for DFS can also go as deep as O(m*n) in the worst case. Therefore, the overall space complexity is O(m*n).
from typing import List
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        found = False
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row,col):
            if row<0 or col<0 or row >= rows or col >= cols or  grid[row][col] != 1:
                return
            queue.append((row,col))
            grid[row][col] = 2
            directions = [(1,0),(0,-1),(-1,0),(0,1)]
            for dx,dy in directions:
                nx,ny = dx+row,dy+col
                dfs(nx,ny)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found:
                break
        directions = [(1,0),(0,-1),(-1,0),(0,1)]
        distance = 0
        while queue:

            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dx,dy in directions:
                    nx,ny = dx+r,dy+c

                    if 0<= nx < rows and 0<= ny < cols:
                        if grid[nx][ny] == 1:
                            return distance
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            queue.append((nx,ny))
            distance += 1
        return distance

