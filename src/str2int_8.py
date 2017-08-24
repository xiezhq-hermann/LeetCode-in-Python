class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        char_list = str.strip()
        char_list += 'p'
        start = char_list[0] in ['-', '+']
        if len(char_list) == 1 or (not char_list[start].isdigit()):
            return 0
        while char_list[start].isdigit():
            start += 1
        return max(-2147483648, min(int(char_list[0:start]), 2147483647))
