# _202. Happy Number


class Solution:
    def isHappy(self, n: int):

        mem_list = [n]

        while True:
            n = self.sum_of_squares(n)

            if n == 1:
                return True
            elif n not in mem_list:
                mem_list.append(n)
            else:
                return False

    def sum_of_squares(self, num):

        result = 0

        while num > 0:
            b = int(num % 10)
            num = int(num / 10)
            result += (b * b)

        return result
