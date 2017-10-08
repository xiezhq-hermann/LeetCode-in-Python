class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        check = n ^ (n >> 1)
        return not check & (check + 1)
