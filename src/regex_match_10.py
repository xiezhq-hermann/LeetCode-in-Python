class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
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

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        table = [[0]*p_len]*s_len
        i, j = 0, 0
        while i < s_len and j < p_len:
            

        self.tried_sets = set()
        return self.match(s, p, 0, 0)

    def match(self, s, p, i, j):
        if (i, j) in self.tried_sets:
            return False
        self.tried_sets.add((i,j))
        if i == len(s) and j == len(p):
            return True

        if i == len(s):
            if j < len(p) - 1 and p[j+1] == '*':
                return self.match(s, p, i, j +2)

        if i < len(s) and j < len(p):
            if j < len(p) - 1 and p[j+1] == '*':
                if self.char_match(s[i], p[j]):
                    return self.match(s, p, i+1, j) or self.match(s, p, i, j+2)
                else:
                    return self.match(s, p, i, j + 2)
            else:
                if self.char_match(s[i], p[j]):
                    return self.match(s, p, i + 1, j + 1)
                else:
                    return False

        return False

    def char_match(self, c1, c2):
        return c1 == c2 or c2 == '.'
