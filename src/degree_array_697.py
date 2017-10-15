class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dic = {}
        for i in range(len(nums)):
            if nums[i] in num_dic:
                num_dic[nums[i]][0][1] = i
                num_dic[nums[i]][1] += 1
            else:
                num_dic[nums[i]] = [[i, i], 1]
        smallest = fre = 0
        for info in num_dic.values():
            if info[1] > fre:
                fre = info[1]
                smallest = info[0][1] - info[0][0] + 1
            elif info[1] == fre:
                smallest = min(info[0][1] - info[0][0] + 1, smallest)
        return smallest
