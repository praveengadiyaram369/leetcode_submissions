# _66. Plus One


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] != 9:
            digits[-1] += 1
        else:
            i = 1
            while i <= len(digits):
                if digits[-i] == 9:
                    digits[-i] = 0
                else:
                    digits[-i] += 1
                    break
                i += 1

            if digits[0] == 0:
                digits.append(0)
                digits[0] = 1

        return digits
