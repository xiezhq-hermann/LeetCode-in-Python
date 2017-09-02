# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        point_remove = ListNode(0)
        point_remove.next = pre
        point_head = ListNode(0)
        point_head.next = head
        for i in range(n - 1):
            point_head.next = point_head.next.next
        while point_head.next.next:
            point_head.next = point_head.next.next
            point_remove = point_remove.next
        point_remove.next.next = point_remove.next.next.next
        return pre.next
