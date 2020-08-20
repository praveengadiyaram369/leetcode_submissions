# _342. Power of Four

# _simple check bits solution


class Solution:

    def check_bits(self, n):
        cnt = 0
        offset = 0

        for i in range(0, 32):
            if n & (1 << i):
                if cnt == 0:
                    cnt += 1
                    offset = i
                else:
                    return False

        return cnt == 1 and offset % 2 == 0

    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and self.check_bits(num)


# _best solution
class Solution:

    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and 0b1010101010101010101010101010101 & num == num
