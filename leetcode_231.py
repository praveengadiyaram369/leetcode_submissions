# _231. Power of Two

# _counting bits solution


class Solution:
    def get_bits(self, n):
        cnt = 0
        for i in range(0, 64):
            if n & (1 << i):
                cnt += 1
        return cnt

    def isPowerOfTwo(self, n: int) -> bool:
        return self.get_bits(n) == 1

# _best solution


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0
