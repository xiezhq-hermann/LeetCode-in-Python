class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x > 0) * 2 - 1
        x = int(str(sign * x)[::-1])
        return (x < 2147483647) * x * sign  # -8463847412 is invalid
