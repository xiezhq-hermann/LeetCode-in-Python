class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        if str_len <= 1:
            return s
        aug_str = '#'.join('^{}$'.format(s))
        # This line is inspired from https://discuss.leetcode.com/topic/10484/manacher-algorithm-in-python-o-n/1 @DiZ

        aug_len = 2*str_len + 3
        len_palin = [1] * aug_len
        len_palin[2], len_palin[-2] = 2, 2
        center, bound = 2, 4
        for i in range(3, aug_len - 3):
            j = 2 * center - i
            if bound > i:
                if bound - i == len_palin[j]:
                    len_palin[i] = bound - i
                    while aug_str[i + len_palin[i]] == aug_str[i - len_palin[i]]:
                        len_palin[i] += 1
                else:
                    len_palin[i] = min(len_palin[j], (bound - i))
            else:
                while aug_str[i + len_palin[i]] == aug_str[i - len_palin[i]]:
                    len_palin[i] += 1
            if len_palin[i] + i >= bound:
                center, bound = i, len_palin[i] + i

        palin_index = len_palin.index(max(len_palin))
        start = (palin_index - len_palin[palin_index] + 1) // 2
        return s[start:start + len_palin[palin_index] - 1]
