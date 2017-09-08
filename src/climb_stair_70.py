class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = pow(5, 0.5)
        phi = (1 + sqrt5) / 2
        return int(round((phi**(n + 1) - (-phi)**(-n - 1)) / sqrt5))
