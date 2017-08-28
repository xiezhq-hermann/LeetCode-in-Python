class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        elif s == '':
            return False
        p += '!'
        p = p.split('*')
        length = len(s)
        piece = len(p)
        j = 0
        for sub in range(piece):
            for i in range(len(p[sub]) - 1):
                if (j == length) or (s[j] != p[sub][i] and p[sub][i] != '.'):
                    return False
                j += 1
            while (j < length) and (p[sub][-1] == s[j] or p[sub][-1] == '.'):
                j += 1
            k = 0
            while sub != piece - 1 and k < len(p[sub + 1]) and j > 0 and p[sub + 1][k] == p[sub][-1] == s[j - 1]:
                k += 1
                j -= 1
        return j == length
