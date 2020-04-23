# _125. Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        numeric = range(47, 58)
        alphabet_cap = range(65, 91)
        alphabet_small = range(97, 123)

        if r < 1:
            return True

        while l < r:

            l_value = ord(s[l])
            r_value = ord(s[r])

            if l_value == 32 or (l_value not in numeric and l_value not in alphabet_cap and l_value not in alphabet_small):
                l += 1
                continue
            if r_value == 32 or (r_value not in numeric and r_value not in alphabet_cap and r_value not in alphabet_small):
                r -= 1
                continue

            if l_value in alphabet_cap:
                l_value -= 65
            if l_value in alphabet_small:
                l_value -= 97

            if r_value in alphabet_cap:
                r_value -= 65
            if r_value in alphabet_small:
                r_value -= 97

            if l_value == r_value:
                l += 1
                r -= 1
            else:
                return False

        return True
