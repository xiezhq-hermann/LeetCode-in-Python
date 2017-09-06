class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        table = [[0 for i in range(p_len + 1)] for i in range(s_len + 1)]
        back_stack = []
        i, j = 0, 0
        while i != s_len or j != p_len:
            if table[i][j]:
                if len(back_stack) > 0:
                    i, j = back_stack.pop()
                    continue
                return False
            table[i][j] = 1
            if i == s_len or j == p_len:
                if i == s_len and j < p_len - 1 and p[j + 1] == '*':
                    j += 2
                elif len(back_stack) > 0:
                    i, j = back_stack.pop()
                else:
                    return False
                continue
            if j < p_len - 1 and p[j + 1] == '*':
                if self.char_match(s[i], p[j]):
                    back_stack.append((i + 1, j))
                j += 2
            elif self.char_match(s[i], p[j]):
                i, j = i + 1, j + 1
            elif len(back_stack) > 0:
                i, j = back_stack.pop()
            else:
                return False
        else:
            return True

    def char_match(self, c1, c2):
        return c1 == c2 or c2 == '.'
