class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(array, length):
            if length <= 1:
                return array
            left_len = length // 2
            right_len = length - left_len
            left = merge(array[:left_len], left_len)
            right = merge(array[left_len:], right_len)
            res = [(0, 0)] * length
            i = j = count = 0
            while i < left_len:
                if j < right_len:
                    if left[i][1] <= right[j][1]:
                        res[i + j] = left[i]
                        small[left[i][0]] += count
                        i += 1
                    else:
                        res[i + j] = right[j]
                        count += 1
                        j += 1
                    continue
                else:
                    for ele in left[i:]:
                        small[ele[0]] += count
                    res[i + j:] = left[i:]
                    break
            else:
                res[i + j:] = right[j:]
            return res

        length = len(nums)
        small = [0] * length
        merge(list(enumerate(nums)), length)
        return small

# if __name__ == "__main__":
#     a = Solution()
#     print(a.countSmaller([5,2,1,6]))
