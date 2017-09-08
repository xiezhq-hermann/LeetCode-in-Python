class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, res = 1, 1
        for a in range(2, n + 1):
            base, res = res, base + res
        return res
