# _58. Length of Last Word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        last_wlen = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and last_wlen > 0:
                return last_wlen
            elif s[i] != ' ':
                last_wlen += 1

        return last_wlen
