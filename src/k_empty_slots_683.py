class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        bloom = [flowers[0]]
        num_bloom = 1
        for slot in flowers[1:]:
            left = 0
            for x in range(num_bloom):
                if bloom[x] > slot:
                    if bloom[x] - slot == k + 1:
                        return num_bloom + 1
                    elif left and slot - left == k + 1:
                        return num_bloom + 1
                    else:
                        bloom.insert(x, slot)
                        break
                else:
                    left = bloom[x]
            else:
                if left and slot - left == k + 1:
                    return num_bloom + 1
                bloom.insert(num_bloom, slot)
            num_bloom += 1
        return -1
