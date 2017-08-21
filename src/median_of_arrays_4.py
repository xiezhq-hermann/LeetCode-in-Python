class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m >= n:
            pass
        else:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        while n > 2:
            cut1, cut2 = m // 2, n // 2
            median1 = nums1[cut1] if m % 2 else (
                nums1[cut1] + nums1[cut1 - 1]) / 2
            if n % 2:
                median2 = nums2[cut2]
            else:
                median2 = (nums2[cut2] + nums2[cut2 - 1]) / 2
                cut2 -= 1
            if median1 > median2:
                nums2 = nums2[cut2:]
                nums1 = nums1[:(m - cut2)]
            elif median1 < median2:
                nums2 = nums2[:(n - cut2)]
                nums1 = nums1[cut2:]
            else:
                return float(median1)
            m -= cut2
            n -= cut2

        target = m // 2
        if n == 2 and m > 2:
            outer0, outer1 = nums2[0], nums2[1]
            if m % 2:
                left = max(outer0, nums1[target - 1])
                right = min(outer1, nums1[target + 1])
                if left <= nums1[target] <= right or right <= nums1[target] <= left:
                    return float(nums1[target])
                elif nums1[target] <= left <= right or right <= left <= nums1[target]:
                    return float(left)
                else:
                    return float(right)
            else:
                left = max(outer0, nums1[target - 2])
                right = min(outer1, nums1[target + 1])
                return (left + right + nums1[target] + nums1[target - 1] - max(left, right, nums1[target], nums1[target - 1]) - min(left, right, nums1[target], nums1[target - 1])) / 2
        elif n == 2 and m == 2:
            return (nums2[0] + nums2[1] + nums1[target] + nums1[target - 1] - max(nums2[0], nums2[1], nums1[target], nums1[target - 1]) - min(nums2[0], nums2[1], nums1[target], nums1[target - 1])) / 2
        elif n == 1 and m > 1:
            outer = nums2[0]
            if m % 2:
                if outer < nums1[target - 1]:
                    return (nums1[target - 1] + nums1[target]) / 2
                elif outer > nums1[target + 1]:
                    return (nums1[target + 1] + nums1[target]) / 2
                else:
                    return (outer + nums1[target]) / 2
            else:
                if outer > nums1[target]:
                    return float(nums1[target])
                elif outer < nums1[target - 1]:
                    return float(nums1[target - 1])
                else:
                    return float(outer)
        elif n == 1 and m == 1:
            return (nums1[0] + nums2[0]) / 2
        else:
            return float(nums1[target]) if m % 2 else (nums1[target] + nums1[target - 1]) / 2
