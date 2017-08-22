class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res_s = [''] * numRows
        target, flag = 0, 1
        for i in s:
            res_s[target] += i
            if target == 0:
                flag = 1
            elif target == numRows - 1:
                flag = -1
            else:
                pass
            target += flag
        return ''.join(res_s)
