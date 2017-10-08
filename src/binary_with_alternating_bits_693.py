class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        check = n ^ (n >> 1)  # check the adjecent two bits
        # if there is no alternative bits, all bits of check will be 1
        return not check & (check + 1)
