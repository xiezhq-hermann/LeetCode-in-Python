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
        j = 0
        for sub in p:
            for i in range(len(sub) - 1):
                if (j == length) or (s[j] != sub[i] and sub[i] != '.'):
                    return False
                j += 1
            while (j < length) and (sub[-1] == s[j] or sub[-1] == '.'):
                j += 1
        return j == length
