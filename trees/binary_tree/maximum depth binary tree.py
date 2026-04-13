#leetcode-104 maximum depth of binary tree
def maxDepth(root) -> int:
    if root == None:
        return 0
    leftmaxdepth = maxDepth(root.left)
    rightmaxdepth = maxDepth(root.right)
    return max(leftmaxdepth, rightmaxdepth) + 1