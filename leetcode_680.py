# _680. Valid Palindrome II


class Solution:

    def check_palindrome(self, s, direction):
        skip_cnt = 0
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                skip_cnt += 1
                if direction == 'left':
                    l += 1
                elif direction == 'right':
                    r -= 1

            if skip_cnt == 2:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:

        return self.check_palindrome(s, 'right') or self.check_palindrome(s, 'left')
