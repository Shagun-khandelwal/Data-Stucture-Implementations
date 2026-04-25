 
# abc -> abc, ab, ac, bc, a, b, c, ""
# time complexity: O(2^n * n) because we are generating 2^n subsets and each subset can take O(n) time to create a string . space complexity: O(n) because we are using a temporary list to store the current subset and the maximum depth of the recursion is n.
def find_all_subsets_backtracking(s):
    res = []
    def backtrack(index,subset):
        if index == len(s):
            res.append("".join(subset))
            return
    
        # include the current character
        subset.append(s[index])
        backtrack(index+1,subset)

        # pop so that we come to normal state
        subset.pop()

        # exclude the current character
        backtrack(index+1,subset)
    backtrack(0,[])
    return res

print(find_all_subsets_backtracking("abc"))