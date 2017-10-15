class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        i = count_bin = 0
        while i < s_len:
            j = i + 2
            while j <= s_len:
                cut = j
                for n in range(i + 1, j):
                    if s[n] != s[n - 1]:
                        if cut == j:
                            cut = n
                        else:
                            break
                else:
                    if j - cut < cut - i:
                        j += 2
                        continue
                    elif j - cut == cut - i:
                        count_bin += 1
                    break
                break
            i += 1
        return count_bin
