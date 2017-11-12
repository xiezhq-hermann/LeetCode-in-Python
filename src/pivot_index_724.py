class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            left, right = 0, sum(nums)
            for i in range(0,len(nums)):
                if i >= 1:
                    left += nums[i-1]
                right -= nums[i]
                if left == right:
                    return i
        return -1
