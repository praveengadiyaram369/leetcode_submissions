# _326. Power of Three


class Solution:

    def check_power(self, t):
        if t == 1:
            return True
        elif t > 0 and t % 3 == 0:
            return self.check_power(t/3)
        else:
            return False

    def isPowerOfThree(self, n: int) -> bool:
        return self.check_power(n)
