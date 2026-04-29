# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
# time complexity: O(m*n*4^k) where m and n are the dimensions of the board and k is the length of the word. space complexity: O(k) because in worst case we can have k recursive calls in the call stack.

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(k,i,j):
            # base case
            if k == len(word):
                return True
            # recursive case
            if i<0 or i>= len(board) or j <0 or j>= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = '' # marking the element as visited

            # moving in all 4 directions (i+1,j),(i-1,j),(i,j-1),(i,j+1)
            if backtrack(k+1,i+1,j) or backtrack(k+1,i-1,j) or backtrack(k+1,i,j-1) or backtrack(k+1,i,j+1):
                return True
            # state back to original for backtracking
            board[i][j] = temp
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0,i,j):
                    return True
        return False