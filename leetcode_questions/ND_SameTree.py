# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Same tree. Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# my first thought when solving this problem was to use a preorder/inorder/postorder traversal and compare each element
# that's essentially what we are doing here with this recursion. The first check is to make sure that we aren't given
# empty binary trees and when we reach the left/right side (and both trees are null) we return True. Finally, we want
# to compare the values, so that's the main property and then we want to compare the values of each tree down its left
# path and then its right path.


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p is not None and q is not None:
            return ((p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        # print(p.val)
        # self.isSameTree(p.right,q)
        # self.isSameTree(p.left,q)
