class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchLeft(low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        def searchRight(low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        left = searchLeft(0, len(nums) - 1, target)
        if left < len(nums) and nums[left] == target:
            return [left, searchRight(0, len(nums) - 1, target)]
        return [-1, -1]
