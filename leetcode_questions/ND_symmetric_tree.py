# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# idea: I knew I needed to check each root.left and root.right, but I initially didn't think about recursing down the right
# node and the left node. the next big idea was understanding I needed to check that the left.right == right.left too.
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: # base case of root is null
            return True
        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (
            left.val == right.val and self.checkSymmetric(left.left,right.right) and self.checkSymmetric(left.right, right.left)
        )
        # else:
        #     if self.isSymmetric(root.left) != self.isSymmetric(root.right):
        #         print("w0w")
        #         return False
        
        # return True
        
