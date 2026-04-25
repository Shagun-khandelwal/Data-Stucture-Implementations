from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def canPlace(x,y,board,n):
            # column
            for k in range(x):
                if board[k][y] == 1:
                    return False
            
            # left diagonal
            i = x
            j = y
            while i>=0 and j>=0:
                if board[i][j]==1:
                    return False
                i-=1
                j-=1
            
            # right diagonal
            i=x
            j=y
            while i>=0 and j<n:
                if board[i][j] == 1:
                    return False
                i-=1
                j+=1
            
            return True



        def solve(n,board,i): #size, board, current_idx
            # base case
            if i == n:
                temp_board = []
                for rows in board:
                    s=""
                    for cell in rows:
                        if cell == 1:
                            s+= "Q"
                        else:
                            s+="."
                    temp_board.append(s)
                res.append(temp_board)
                return
            
            # recursive case
            for j in range(n):
                if (canPlace(i,j,board,n)):

                    board[i][j] = 1

                    solve(n,board,i+1)
                    
                    # backtracking
                    board[i][j] = 0

        
        res = []
        board = [[0]*n for _ in range(n)]
        solve(n,board,0)

        return res

            
            
