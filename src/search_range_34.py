class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return [-1, -1]

        low = high = mid
        while low > 0 and nums[low - 1] == target:
            low -= 1
        while high < len(nums) - 1 and nums[high + 1] == target:
            high += 1

        return [low, high]
