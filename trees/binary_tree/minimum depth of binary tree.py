#leetcode-111 Minimum Depth of binary tree
def minDepth(root) -> int:
    if root == None:
        return 0
    leftmin = minDepth(root.left)
    rightmin =minDepth(root.right)
    mini = min(leftmin, rightmin) + 1
    maxi = max(leftmin, rightmin) + 1
    if mini == 1 and maxi > 1:
        return maxi
    return mini