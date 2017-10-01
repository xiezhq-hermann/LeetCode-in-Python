# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def countPath(node):
            if not node:
                return 0
            left_path = countPath(node.left)
            right_path = countPath(node.right)
            flag = 0
            if node.left and node.left.val == node.val:
                left_path += 1
            else:
                left_path = 0
            if node.right and node.right.val == node.val:
                right_path += 1
            else:
                right_path = 0
            self.longest = max(self.longest, left_path + right_path)
            return max(left_path, right_path)

        countPath(root)
        return self.longest
