# _190. Reverse Bits


class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0

        for val in range(31, -1, -1):
            if n & (1 << val) > 0:
                result += (2 ** (31 - val))

        return result
