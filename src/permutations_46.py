class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        return [[n] + sub for i, n in enumerate(nums) for sub in self.permute(nums[:i] + nums[i + 1:])]
