# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # print(root)
        mydict={}
        def preorder(root,row,col):
            if root:
                if col in mydict.keys():
                    mydict[col].append((row,root.val))
                else:
                    mydict[col]=[(row,root.val)]
                print(root.val,row,col)
                preorder(root.left,row+1,col-1)
                preorder(root.right,row+1,col+1)
        preorder(root,0,0)
        print(mydict)
        res=[]
        for k in sorted(mydict.keys()):
            curr_list = sorted(mydict[k])
            temp_list=[]
            for row,val in curr_list:
                temp_list.append(val)
            res.append(temp_list)
        return res