# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True

        if p is not None and q is not None:
            # the roots must be equal, as well as their left and right subtrees
            return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        return False

