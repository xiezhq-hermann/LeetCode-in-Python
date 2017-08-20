# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        res = ListNode(0)
        start.next = res
        bit = 0
        while l1 and l2:
            res.next = ListNode(l1.val+l2.val+bit)
            res = res.next
            if res.val < 10:
                bit = 0
            else:
                bit = 1
                res.val -= 10
            l1, l2 = l1.next, l2.next
        res.next = l1 if l1 else l2
        while bit:
            if res.next:
                res.next.val += 1
                res = res.next
                if res.val < 10:
                    bit = 0
                else:
                    bit = 1
                    res.val -= 10
            else:
                res.next = ListNode(1)
                break
        return start.next.next


def initial(nums):
    start = ListNode(0)
    res = ListNode(nums[0])
    start.next = res
    for i in nums[1:]:
        res.next = ListNode(i)
        res = res.next
    return start.next

def traversal(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)
