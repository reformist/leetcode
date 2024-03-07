# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Path Sum: Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# I knew to update targetSum and return true if I was at the end of the tree and sum was zero. however, I didn't know
# how to check every tree. the way to do it is definitely check if root.left and root.right is None and then recursing on both the left and right sides of three
#
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return False
        print(targetSum)
        targetSum = targetSum - root.val

        if root.left is None and root.right is None:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


        
