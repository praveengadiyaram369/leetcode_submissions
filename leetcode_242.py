# _242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        elif len(s) == 0:
            return True

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for char in alphabet:
            if s.count(char) != t.count(char):
                return False

        return True
