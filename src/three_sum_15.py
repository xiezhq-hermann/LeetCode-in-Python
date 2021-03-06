class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        solution = []
        dic_num = dict()
        nums.sort()

        for i in range(length):
            dic_num[nums[i]] = i

        i = 0
        while i < length and nums[i] <= 0:
            target = -(nums[i])
            end = length
            j = i + 1
            while j < end:
                reside = target - nums[j]
                if reside in dic_num and dic_num[reside] > j:
                    solution.append([nums[i], nums[j], reside])
                    end = dic_num[reside]
                j = dic_num[nums[j]] + 1
            i = dic_num[nums[i]] + 1

        return solution
