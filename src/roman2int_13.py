class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        values = {'M': 1000, 'D': 500, 'C': 100,
                  'L': 50, 'X': 10, 'V': 5, 'I': 1}
        left = 1000
        for i in s:
            integer = integer + values[i] - 2 * (left < values[i]) * left
            left = values[i]
        return integer
