class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        index_dic = {}
        i = -1
        j = 0

        for i in range(len(s)):
            target = s[i]
            if target in index_dic and j<=index_dic[target]:
                max_len = max(i-j, max_len)
                j = index_dic[target] + 1
            index_dic[target] = i
        else:
            return max(i-j+1, max_len)
