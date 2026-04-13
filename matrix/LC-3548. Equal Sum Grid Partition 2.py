# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

# Each of the two resulting sections formed by the cut is non-empty.
# The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
# If a cell is discounted, the rest of the section must remain connected.
# Return true if such a partition exists; otherwise, return false.

# Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
    #    mydict = {2:[(i1,j1), (i2,j2)]}
# mydict = {
#     2:
#     {
#     "rows": {1:[1,2,3,4], 4:[2,6,8]},
#     "cols": {2:[1, 2, 4]}
#     },
#     3:
#     {
#     "rows": {1:[1,2]},
#     "cols": {1:[1], 2:[1]}
#     }
        # pre compute sum of rows
        rows = len(grid)
        columns = len(grid[0])
        print(rows)
        sum_rows = [0]*rows
        sum_columns = [0] * columns

        for r in range(rows):
            temp_sum = 0
            for c in range(columns):
                temp_sum += grid[r][c]
            sum_rows[r] += temp_sum if r == 0 else temp_sum + sum_rows[r-1]
        
        # pre compute sum of columns
        for c in range(columns):
            temp_sum = 0
            for r in range(rows):
                temp_sum += grid[r][c]
            sum_columns[c] += temp_sum if c==0 else temp_sum + sum_columns[c-1]

        # making dictionary to check elements

        mydict = dict()
        for r in range(rows):
            for c in range(columns):
                val = grid[r][c]
                if val not in mydict:
                    mydict[val] = {"rows":{},"columns":{}}
                
                # add to rows dictionary
                if r not in mydict[val]["rows"]:
                    mydict[val]["rows"][r]=[]
                mydict[val]["rows"][r].append(c)

                # add to columns dictionary

                if c not in mydict[val]["columns"]:
                    mydict[val]["columns"][c]=[]
                mydict[val]["columns"][c].append(r)
        
        # print(mydict)

        def helper_rows(diff,r1,r2):
            # if diff not exists
            if diff not in mydict:
                return False
            
            rows_dict = mydict[diff]["rows"]

            for i in rows_dict.keys():
                if r1 <= i < r2:
                    cols_list = rows_dict[i]

                    # if number of rows and columns != 1 then you can remove any element

                    if r2-r1 > 1 and columns != 1:
                        return True

                    # if number of columns == 1 then we can only remove upper and lower element
                    for j in cols_list:
                        if j == 0 or j == columns -1:
                            if i == r1 or i == r2-1:
                                print("ye hai",j,diff)
                                return True  
            return False

        def helper_columns(diff,c1,c2):
            print("helper columns")
            if diff not in mydict:
                return False
            
            cols_dict = mydict[diff]["columns"]

            for j in cols_dict.keys():
                if c1 <= j < c2:
                    rows_list = cols_dict[j]
                    # if number of rows and columns > 1 then we can remove any element
                    if c2-c1 > 1 and rows != 1:
                        return True
                    print("ds")
                    # if number of rows == 1 then we can only remove left most or right most element
                    print(rows_list)
                    for i in rows_list:
                        if i== 0  or i == rows -1:
                            if j == c1 or j == columns -1:
                                return True
            return False

        # checking partitions by rows first
        for r in range(rows):
            # check if number of rows ==1 , then we can't divides
            if rows == 1:
                break
            fp_sum = sum_rows[r]
            sp_sum = sum_rows[-1] - fp_sum
            diff = abs(sp_sum - fp_sum)

            if diff == 0:
                return True

            if sp_sum > fp_sum:
                if helper_rows(diff,r+1,rows):
                    return True
            else:
                if helper_rows(diff,0,r+1):
                    return True
        
        # checking partitions by columns now
        for c in range(columns):
            if columns == 1:
                break
            fp_sum = sum_columns[c]
            sp_sum = sum_columns[-1] - fp_sum
            diff = abs(sp_sum - fp_sum)

            if diff == 0:
                return True
            
            if sp_sum > fp_sum:
                if helper_columns(diff,c+1,columns):
                    return True
            else:
                if helper_columns(diff,0,c+1):
                    return True

        return False

 