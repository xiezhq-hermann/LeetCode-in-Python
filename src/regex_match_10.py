class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        elif p == '':
            return False
        else:
            j = 0
            for i in range(len(p)):
                if i == len(p) - 1 or p[i + 1] != '*':
                    if len(s) == 0 or (p[i] != s[j] and p[i] != '.'):
                        return False
                    else:
                        return self.isMatch(s[j + 1:], p[i + 1:])
                else:
                    if self.isMatch(s[j:], p[i + 2:]):
                        return True
                    else:
                        while j < len(s) and (s[j] == p[i] or p[i] == '.'):
                            j += 1
                            if self.isMatch(s[j:], p[i + 2:]):
                                return True
                        return False
            return False
