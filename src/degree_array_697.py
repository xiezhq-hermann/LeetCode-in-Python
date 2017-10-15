class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counts = Counter(nums).most_common()
        i = 0
        num_len = smallest = len(nums)
        while i < len(counts) and counts[i][1] == counts[0][1]:
            element, fre = counts[i]
            flag = -1
            for j in range(num_len):
                if nums[j] == element:
                    if flag == -1:
                        flag = j
                    fre -= 1
                    if fre == 0:
                        smallest = min(j+1 - flag, smallest)
                        break
            i += 1
        return smallest
