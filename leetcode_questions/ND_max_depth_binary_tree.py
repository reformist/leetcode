# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Given the root of a binary tree, return its maximum depth.
# general idea: believe in the power of recursion. if root is null, return null. however, the count only begins
# when there is a second node to the left or right of the root node, so need to add one after recursing on the right
# and left subtrees. then need to find the max of them


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            right_length = self.maxDepth(root.left)
            left_length = self.maxDepth(root.right)

            if right_length > left_length:
                return right_length + 1
            else:
                return left_length + 1
        

        
