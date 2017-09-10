class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length

        self.nums = nums
        self.num_dic = {1: 1}
        self.sub_length = [-1] * length
        self.sub_num = [1] * length

        def recur(index, nums):
            if nums == []:
                return 1

            sub_length = sub_num = 1
            for i in range(len(nums)):
                tem = 0
                if nums[i] > self.nums[index]:
                    if self.sub_length[index + i + 1] != -1:
                        tem = 1 + self.sub_length[index + i + 1]
                    else:
                        tem = 1 + recur(index + i + 1, nums[i + 1:])

                    if tem >= sub_length > 0:
                        if tem > sub_length:
                            sub_length = tem
                            sub_num = self.sub_num[index + i + 1]
                        else:
                            sub_num += self.sub_num[index + i + 1]

            self.sub_length[index] = sub_length
            self.sub_num[index] = sub_num
            if sub_length in self.num_dic:
                self.num_dic[sub_length] += sub_num
            else:
                self.num_dic[sub_length] = sub_num

            return sub_length

        n, longest = 0, 1
        while n <= length - longest:
            if self.sub_length[n] == -1:
                longest = max(longest, recur(n, nums[n + 1:]))
            n += 1
        return self.num_dic[longest]
