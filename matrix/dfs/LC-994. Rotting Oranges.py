# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# using BFS instead of DFS because at every minute we have to process every orange that is rotten on previous minute for example if 2 fresh orange becomes rotten in the previous minute then we have to process or apply our funtion on those 2 rotten oranges in a single minute. It's like a chainning virus system.
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges +=1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        if fresh_oranges == 0:
            return 0
        directions = [(1,0),(0,-1),(-1,0),(0,1)]

        while len(queue) > 0 and fresh_oranges > 0:
            minutes +=1

            for _ in range(len(queue)):
                r,c  = queue.popleft()
                for dx,dy in directions:
                    nx,ny = r+dx,c+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                        fresh_oranges -=1
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
        return minutes if fresh_oranges == 0 else -1
