# _172. Factorial Trailing Zeroes


class Solution:
    def trailingZeroes(self, n: int) -> int:

        result = 0
        div = 1
        k = (5 ** div)

        while k <= n:
            result += int(n / k)
            div += 1
            k = (5 ** div)

        return result
