# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        rand_int = random.randint(0,2147483647)

        tem = self.head
        count = 0
        while count < rand_int and tem:
            tem = tem.next
            count += 1
            if not tem:
                break
        else:
            return tem.val

        target = rand_int % count

        tem = self.head
        while target > 0:
            tem = tem.next
            target -= 1
        return tem.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
