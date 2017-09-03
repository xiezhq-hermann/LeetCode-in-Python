#
# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
#
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minimum = -1
        while root.left:
            if root.val < root.left.val <= root.right.val:
                return root.left.val
            elif root.val < root.right.val <= root.left.val:
                return root.right.val
            elif root.val == root.right.val < root.left.val:
                minimum = self.findSecondMinimumValue(root.right)
                return min(minimum,root.left.val) if minimum != -1 else root.left.val
            elif root.val == root.left.val < root.right.val:
                minimum = self.findSecondMinimumValue(root.left)
                return min(minimum,root.right.val) if minimum != -1 else root.right.val
            else:
                minimum = min(self.findSecondMinimumValue(root.left), self.findSecondMinimumValue(root.right))
                return minimum if minimum != -1 else max(self.findSecondMinimumValue(root.left), self.findSecondMinimumValue(root.right))
        return minimum
