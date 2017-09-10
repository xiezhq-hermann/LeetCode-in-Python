class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        tem = longest = 1
        for i in range(1,length):
            if nums[i] > nums[i-1]:
                tem += 1
            else:
                longest = max(tem, longest)
                tem = 1
        return longest if longest >= tem else tem
