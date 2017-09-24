class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [1] * n

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = 0

        return sum(primes) - 2
