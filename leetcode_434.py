# _434. Number of Segments in a String

# _Approach 1


class Solution:
    def countSegments(self, s: str) -> int:

        s = s.strip()
        if len(s) == 0:
            return 0

        space_fnd = False
        space_cnt = 0

        for char in s:
            if char == ' ':
                if space_fnd is False:
                    space_fnd = True
                    space_cnt += 1
                continue
            space_fnd = False

        return space_cnt + 1

# _Approach 2


class Solution:
    def countSegments(self, s: str) -> int:

        word_cnt = 0

        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                word_cnt += 1

        return word_cnt
