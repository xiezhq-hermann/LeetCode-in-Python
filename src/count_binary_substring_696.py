class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        count = start = cut = 0
        for i in range(1,s_len):
            if s[i] != s[i-1]:
                cut = i - start
                count += 1
                start = i
            else:
                if i - start < cut:
                    count += 1
        return count
