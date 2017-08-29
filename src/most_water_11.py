class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        flag, water = 0, 0
        while (right - left) > 0:
            if height[left] <= flag or height[right] <= flag:
                left += height[left] <= flag
                right -= height[right] <= flag
            elif height[left] <= height[right]:
                flag = height[left]
                water = max(water, height[left] * (right - left))
                # right -= height[right] == height[left]
                left += 1
            else:
                flag = height[right]
                water = max(water, height[right] * (right - left))
                right -= 1
        return water
