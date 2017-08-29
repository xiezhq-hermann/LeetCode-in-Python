class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        flag, water = 0, 0
        while (right - left) > 0:
            short = min(height[left], height[right])
            water = max(water, short * (right - left))
            right -= (height[right] <= flag or height[right] <= short)
            left += (height[left] <= flag or height[left] <= short)
            flag = max(short, flag)
        return water
