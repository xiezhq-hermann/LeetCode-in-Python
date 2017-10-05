class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        water = flag = gradient = 0
        left = right = height[0]
        tem = [left]
        height.append(0)
        for i in height[1:]:
            gradient = i - right
            if gradient >= 0 or flag:
                if gradient >= 0 :
                    flag = 0
                tem.append(i)
            else:
                left_inx, right_inx = 0, -1
                if left > right:
                    while tem[left_inx] > right:
                        left_inx += 1
                        left = tem[left_inx - 1]
                if left < right:
                    while tem[right_inx - 1] > left:
                        right_inx -= 1
                water += min(left, tem[right_inx])*len(tem[left_inx:right_inx])-sum(tem[left_inx:right_inx])
                flag = 1
                tem = [right, i]
                left = right
            right = i
        return water
