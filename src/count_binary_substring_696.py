class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        i = count_bin = 0
        while i < s_len:
            j = i
            while j < s_len:
                if (j+1 - i)%2:
                    j += 1
                    continue
                count = 0
                flag = False
                for n in range(i+1, j+1):
                    if s[n] != s[n-1]:
                        if not flag:
                            count = n
                            flag = True
                        else:
                            break
                else:
                    if j+1-i == 2*(count-i):
                        count_bin += 1
                        break
                    j += 1
                    continue
                break
            i += 1
        return count_bin
