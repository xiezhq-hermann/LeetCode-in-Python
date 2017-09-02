class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        solution = []
        dic_num = dict()
        nums.sort()

        for i in range(length):
            dic_num[nums[i]] = i

        i = 0
        while i < length - 3:
            j = i + 1
            while j < length - 2:
                end = length - 1
                k = j + 1
                while k < end:
                    reside = target - nums[i] - nums[j] - nums[k]
                    if reside in dic_num and dic_num[reside] > k:
                        solution.append([nums[i], nums[j], nums[k], reside])
                        end = dic_num[reside]
                    k = dic_num[nums[k]] + 1
                j = dic_num[nums[j]] + 1
            i = dic_num[nums[i]] + 1

        return solution
