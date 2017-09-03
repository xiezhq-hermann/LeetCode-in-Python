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

    def merge2Lists(self, list1, list2):
        if not list2:
            return list1

        head, point = ListNode(0), ListNode(0)
        head.next = list1
        point.next = head
        while list1 and list2:
            if list1.val <= list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next.next = list2
                list2 = list1
                list1 = point.next.next
        point.next.next = list2
        return head.next

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
