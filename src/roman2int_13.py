class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        s = ' ' + s
        for i in range(1, len(s)):
            integer = integer + 1000 * (s[i] == 'M') + 500 * (s[i] == 'D') + 100 * (s[i] == 'C')\
                + 50 * (s[i] == 'L') + 10 * (s[i] == 'X') + 5 * (s[i] == 'V') + (s[i] == 'I')\
                - 200 * (s[i - 1] == 'C' and (s[i] == 'M' or s[i] == 'D'))\
                - 20 * (s[i - 1] == 'X' and (s[i] == 'C' or s[i] == 'L'))\
                - 2 * (s[i - 1] == 'I' and (s[i] == 'X' or s[i] == 'V'))
        return integer
