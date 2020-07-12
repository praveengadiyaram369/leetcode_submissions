# _509. Fibonacci Number


class Solution:
    def fib(self, N: int) -> int:

        if N == 0:
            return 0
        elif N == 1:
            return 1

        a = 0
        b = 1

        while N >= 2:
            a, b = b, a+b
            N -= 1

        return b
