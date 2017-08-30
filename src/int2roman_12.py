class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousand, hundred, ten, one = num // 1000, (num //
                                                    100) % 10, (num // 10) % 10, num % 10
        roman = 'M' * thousand + ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'][hundred] + ['', 'X', 'XX',
                                                                                                          'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'][ten] + ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'][one]

        return roman
