# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat),len(mat[0])
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        print(mat)
        directions = [(1,0),(0,-1),(-1,0),(0,1)]
        while queue:
            r,c = queue.popleft()
            for dx,dy in directions:
                nx,ny = dx+r,dy+c
                if 0 <= nx < rows and 0<=ny<cols and mat[nx][ny] == -1:
                    mat[nx][ny] = mat[r][c] + 1
                    queue.append((nx,ny))        
        return mat

        

