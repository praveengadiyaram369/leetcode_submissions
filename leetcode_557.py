# _557. Reverse Words in a String III


class Solution:
    def reverseWords(self, s: str) -> str:

        l = r = 0
        result = ''
        s = s.strip()

        for char in s:
            if char != ' ':
                r += 1
            else:
                space_index = r + 1
                while l < r:
                    r -= 1
                    result += s[r]

                l = r = space_index
                result += ' '

        if r == len(s) and r-l > 0:
            while l < r:
                r -= 1
                result += s[r]

        return result
