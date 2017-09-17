class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        count = 1
        for i in range(3,n):
            ceil = int(i**0.5) + 1
            if all(i % j !=0 for j in range(2, ceil)):
                count += 1
        return count
