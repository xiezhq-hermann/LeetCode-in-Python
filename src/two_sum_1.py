class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic_num = dict()
        for i in range(len(nums)):
            if nums[i] in dic_num:
                return [i, dic_num[nums[i]]]
            else:
                dic_num[target-nums[i]] = i
        else:
            return None
