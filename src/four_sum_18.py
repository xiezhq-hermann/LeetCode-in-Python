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
        end = length
        while i < end - 3 and (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]) <= target:
            j = i + 1
            while j < end - 2  and (nums[j] + nums[j + 1] + nums[j + 2] <= target - nums[i]):
                end = length
                k = j + 1
                while k < end - 1:
                    reside = target - nums[i] - nums[j] - nums[k]
                    if reside in dic_num and dic_num[reside] > k:
                        solution.append([nums[i], nums[j], nums[k], reside])
                        end = dic_num[reside]
                    k = dic_num[nums[k]] + 1
                j = dic_num[nums[j]] + 1
            i = dic_num[nums[i]] + 1

        return solution
