#  n=2 -> [()(), (())]

def generateParenthesis(n,open_count,close_count,curr_str):
    # base case
    if len(curr_str) == 2*n:
        res.append(curr_str)
        return
    # recursive case
    if open_count < n:
        generateParenthesis(n,open_count+1,close_count,curr_str+"(")
    if close_count < open_count:
        generateParenthesis(n,open_count,close_count+1,curr_str+")")


res = []
generateParenthesis(3,0,0,"")
print(res)

