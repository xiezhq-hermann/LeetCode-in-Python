class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x % 10 == 0:
            if x == 0:
                return True
            return False
        half_x = 0
        while x > half_x:
            half_x = half_x * 10 + x % 10
            x = x // 10
        else:
            return x == half_x or x == half_x // 10
