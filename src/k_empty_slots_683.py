class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        residue = num_slot = len(flowers)
        bloom = [0] * (num_slot + 1)
        days = 0

        while residue > k:
            slot = flowers[days]
            days += 1
            if bloom[slot]:
                continue

            bloom[slot] = 1
            left, right = slot - k - 1, slot + k + 1
            residue -= 1

            if left > 0 and bloom[left]:
                for i in range(left + 1, slot):
                    if bloom[i]:
                        break
                    bloom[i] = 1
                    residue -= 1
                else:
                    return days

            if right <= num_slot and bloom[right]:
                for i in range(slot + 1, right):
                    if bloom[i]:
                        break
                    bloom[i] = 1
                    residue -= 1
                else:
                    return days

        return -1
