# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque
 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        changed = False
        nom=0
        queue=deque()
        fresh_oranges = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] ==  2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                dx,dy = queue.popleft()
                for nx,ny in directions:
                    ad_x = nx+dx
                    ad_y = ny+dy
                    if 0<=ad_x<rows and 0<=ad_y<columns:
                        if grid[ad_x][ad_y] == 1:
                            grid[ad_x][ad_y] = 2
                            fresh_oranges -= 1
                            queue.append((ad_x,ad_y))
            nom+=1
        return nom if fresh_oranges == 0 else -1

