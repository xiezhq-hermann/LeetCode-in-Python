class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        s = ' ' + s
        for i in range(1, len(s)):
            if s[i] == 'M':
                integer += 1000
                integer -= 200 * (s[i - 1] == 'C')
            elif s[i] == 'D':
                integer += 500
                integer -= 200 * (s[i - 1] == 'C')
            elif s[i] == 'C':
                integer += 100
                integer -= 20 * (s[i - 1] == 'X')
            elif s[i] == 'L':
                integer += 50
                integer -= 20 * (s[i - 1] == 'X')
            elif s[i] == 'X':
                integer += 10
                integer -= 2 * (s[i - 1] == 'I')
            elif s[i] == 'V':
                integer += 5
                integer -= 2 * (s[i - 1] == 'I')
            elif s[i] == 'I':
                integer += 1
        return integer
