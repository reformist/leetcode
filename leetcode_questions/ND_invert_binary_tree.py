# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#  Given the root of a binary tree, invert the tree, and return its root.
# Base case: if root is null, return None.
# My first thought was how would I do this iteratively. I would create a temp node that would equal left node, set
# node.left = node.right and then node.right = node.temp. From there, I needed to figure out the recursive instance
# the big idea was to recurse on temp because if i recursed on node.left, i lost the values of the left/right side
# of the trees.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # given root of binary tree, invert the tree, and return its root
        if not root:
            return None

        temp_val = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp_val)

        return root
