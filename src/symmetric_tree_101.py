# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkTree(root1, root2):
            if root1 and root2:
                if root1.val == root2.val:
                    return checkTree(root1.left, root2.right) and checkTree(root1.right, root2.left)
                return False
            return not (root1 or root2)
        if root:
            return checkTree(root.left, root.right)
        return True
