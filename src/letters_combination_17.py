from functools import reduce


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return [] if digits == '' else reduce(lambda a, b: [x + y for x in a for y in letter_map[b]], digits, [''])
