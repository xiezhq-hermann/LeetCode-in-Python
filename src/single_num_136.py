class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for i in nums:
            single ^= i
        return single
