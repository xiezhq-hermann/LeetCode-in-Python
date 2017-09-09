class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = largest = nums[0]
        for i in nums[1:]:
            if sub <= 0:
                largest = max(i, largest)
                sub = i
            else:
                sub += i
                largest = max(sub, largest)
        return largest
