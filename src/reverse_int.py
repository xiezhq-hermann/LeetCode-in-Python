class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        x = -int(x[-1:0:-1]) if x[0] == '-' else int(x[::-1])
        return x if 2147483647 > x > -2147483648 else 0
