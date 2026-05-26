# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# time complexity: O(n^2) where n is the number of cities
# space complexity: O(n) in worst case when all cities are directly or indirectly connected
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            
            for neighbour in range(city_length):
                if isConnected[city][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)


        city_length = len(isConnected)
        total_provinces = 0
        visited = set()
        for city in range(city_length):
                if city not in visited:
                    total_provinces += 1
                    dfs(city)
        return total_provinces