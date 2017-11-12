# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        import math
        initial,length = root, 0
        divide = [0] * k
        res = [[] for i in range(k)]

        while initial:
            length += 1
            initial = initial.next

        for i in range(k):
            part = math.ceil(length/(k-i))
            divide[i] = part
            length -= part

        head = root
        index = 0
        for num in divide:
            while num > 0:
                res[index].append(head.val)
                num -= 1
                head = head.next
            index += 1

        return res
