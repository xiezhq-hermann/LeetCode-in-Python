class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return ['', 'M', 'MM', 'MMM'][num // 1000]\
            + ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'][(num // 100) % 10]\
            + ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'][(num // 10) % 10]\
            + ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'][num % 10]
