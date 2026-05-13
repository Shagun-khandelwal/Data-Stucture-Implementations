# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

# time complexity is O(m*n) because we are doing DFS for every cell in the grid and each cell will be visited at most once in each DFS. So the overall time complexity is O(m*n).
# space complexity is O(m*n) because in the worst case, we might have to store all the cells in the visited set for both Pacific and Atlantic oceans. Additionally, the recursion stack for DFS can also go as deep as O(m*n) in the worst case. Therefore, the overall space complexity is O(m*n).
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        rows = len(heights)
        cols = len(heights[0])
        def dfs(row,col,visited,prevHeight):
            # (r,c) not in visited , out of bound check, less than previous one
            if (row,col) in visited or row<0 or row >= rows or col < 0 or col >= cols or heights[row][col] < prevHeight:
                return
            visited.add((row,col))
            directions = [(1,0),(0,-1),(-1,0),(0,1)]

            for dx,dy in directions:
                nx,ny = dx+row,dy+col
                dfs(nx,ny,visited,heights[row][col])

        pacific,atlantic = set(),set()
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c]) # pacific top one
            dfs(rows-1,c,atlantic,heights[rows-1][c]) # atlantic bottom one
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0]) # pacific left one
            dfs(r,cols-1,atlantic,heights[r][cols-1]) # atlantic right one
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
        return result