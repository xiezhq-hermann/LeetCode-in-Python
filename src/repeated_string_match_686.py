class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        set_a, set_b = set(A), set(B)
        if set_b > set_a:
            return -1

        for i in range(1, 10000//len(A) + 1):
            multiply = A*i
            if B in multiply:
                return i
        else:
            return -1
