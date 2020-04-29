# _168. Excel Sheet Column Title


class Solution:
    def convertToTitle(self, n: int) -> str:

        capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''

        while n > 0:
            letter = int((n-1) % 26)
            result += capital_letters[letter]

            n = int((n-1)/26)

        return result[::-1]
