# _204. Count Primes


class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1:
            return 0

        primes = [1] * n
        primes[1] = 0
        val = 2

        while (val * val) < n:

            if primes[val] == 1:
                i = (2 * val)
                while i < n:
                    primes[i] = 0
                    i += val

            val += 1

        return sum(primes[1:])
