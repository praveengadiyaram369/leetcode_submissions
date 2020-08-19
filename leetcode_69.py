# _69. Sqrt(x)


class Solution:

    def check_square(self, low, high, x):
        mid = int((low+high)/2)
        square = mid * mid
        if square == x or high - low == 1:
            return mid
        elif mid * mid > x:
            return self.check_square(low, mid, x)
        elif mid * mid < x:
            return self.check_square(mid, high, x)

    def mySqrt(self, x: int) -> int:
        return self.check_square(1, x, x)
