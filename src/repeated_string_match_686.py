class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        base = (len(B)-1)//len(A) + 1
        for i in range(base, base+2):
            if B in A*i:
                return i
        else:
            return -1
