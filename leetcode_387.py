# _387. First Unique Character in a String


class Solution:
    def firstUniqChar(self, s: str) -> int:

        if len(s) == 0:
            return -1

        char_freq = {}

        for idx, char in enumerate(s):

            if char in char_freq:
                char_freq[char] = len(s)
            elif char not in char_freq:
                char_freq[char] = idx

        char_index = min(char_freq.values())
        if char_index == len(s):
            return -1
        return char_index
