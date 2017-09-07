class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= target:
                if nums[mid] > target or nums[mid] <= nums[high] < nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] or nums[mid] >= nums[low] > nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            return -1
