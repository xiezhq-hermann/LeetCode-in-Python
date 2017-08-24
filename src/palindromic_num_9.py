class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        digit = 1
        while x // (10 * digit):
            digit *= 10

        while digit >= 10:
            if x % 10 != x // digit:
                return False
            x = (x % digit) // 10
            digit = digit // 100
        return True
