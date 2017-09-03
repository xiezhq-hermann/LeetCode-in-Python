# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head, point = ListNode(0), ListNode(0)
        head.next = point
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next.next

    # def merge2Lists_recur(self, list1, list2):
    #     if not list1:
    #         return list2
    #     if not list2:
    #         return list1
    #
    #     if list1.val <= list2.val:
    #         list1.next = self.merge2Lists(list1.next, list2)
    #         return list1
    #     else:
    #         list2.next = self.merge2Lists(list2.next, list1)
    #         return list2

# def mergeKLists(self, lists):
#     """
#     :type lists: List[ListNode]
#     :rtype: ListNode
#     """
#     self.nodes = []
#     head, point = ListNode(0), ListNode(0)
#     head.next = point
#
#     for l in lists:
#         while l:
#             self.nodes.append(l.val)
#             l = l.next
#
#     for x in sorted(self.nodes):
#         point.next = ListNode(x)
#         point = point.next
#
#     return head.next.next

# from Queue import PriorityQueue
#
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         head, point = ListNode(0), ListNode(0)
#         head.next = point
#         q = PriorityQueue()
#         for l in lists:
#             if l:
#                 q.put((l.val, l))
#         while not q.empty():
#             val, node = q.get()
#             point.next = ListNode(val)
#             point = point.next
#             node = node.next
#             if node:
#                 q.put((node.val, node))
#         return head.next.next
