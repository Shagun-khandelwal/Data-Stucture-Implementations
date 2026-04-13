# LeetCode 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def preorder(self):
        if self == None:
            return
        elements=[]
        elements += [self.val]
        if self.left:
            elements += self.left.preorder()
        if self.right :
            elements += self.right.preorder()
        return elements
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        return self.myfunc(nums, 0, len(nums) - 1)

    def myfunc(self, nums, start, end):
        if start > end:
            return None
        else:
            mid = (start + end) // 2
            temp = TreeNode(nums[mid])

            temp.left = self.myfunc(nums, start, mid - 1)

            temp.right = self.myfunc(nums, mid + 1, end)

            return temp
Obj = Solution()
nums=[-10,-3,0,5,9]
tree = Obj.sortedArrayToBST(nums)
print(tree.preorder())
