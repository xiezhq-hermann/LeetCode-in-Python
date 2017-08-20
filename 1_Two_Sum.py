class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_num = set(nums)
        for i in hash_num:
            j = target - i
            if j in hash_num:
                zero = nums.index(i)
                nums[zero] = None
                if j in nums:
                    one = nums.index(j)
                    return [zero, one]
                else:
                    continue
            else:
                continue
