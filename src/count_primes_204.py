class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [1] * n
        count = n - 2

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    if primes[j]:
                        count -= 1
                    primes[j] = 0

        return max(count, 0)
