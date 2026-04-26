#  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def balancedParantheses(open_count,close_count,curr_str):
            # base case
            if len(curr_str) == 2*n:
                res.append(curr_str)
                return
            
            # recursive case
            if open_count<n:
                balancedParantheses(open_count+1,close_count,curr_str+"(")
            if close_count < open_count:
                balancedParantheses(open_count,close_count+1,curr_str+")")
        balancedParantheses(0,0,"")
        return res
