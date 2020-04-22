# _28. Implement strStr()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) < 1:
            return 0
        elif len(haystack) < 1:
            return -1

        h = n = 0
        str_index = -1

        while h < len(haystack) and n < len(needle):

            if haystack[h] != needle[n] and str_index == -1:
                h += 1
            elif haystack[h] != needle[n] and str_index != -1:
                h = str_index + 1
                str_index = -1
                n = 0
            elif haystack[h] == needle[n]:
                if str_index == -1:
                    str_index = h
                h += 1
                n += 1

        if n == len(needle):
            return str_index

        return -1
