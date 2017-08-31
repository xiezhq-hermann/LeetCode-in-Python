class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        nums.sort()
        loss = target - (nums[0] + nums[1] + nums[2])

        for i in range(length-2):
            left = i + 1
            right = length - 1
            while left < right:
                new_loss = target - nums[i] - nums[left] - nums[right]
                if new_loss > 0:
                    left += 1
                elif new_loss < 0:
                    right -= 1
                else:
                    return target
                if abs(new_loss) < abs(loss):
                    loss = new_loss
        return target - loss
