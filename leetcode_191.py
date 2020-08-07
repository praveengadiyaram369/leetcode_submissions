# _191. Number of 1 Bits


class Solution:
    def hammingWeight(self, n: int) -> int:

        result = 0

        for val in range(0, 32):
            if n & (1 << val) > 0:
                result += 1

        return result
