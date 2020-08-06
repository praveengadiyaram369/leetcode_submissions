# _13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:

        sub_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        add_dict = {"I": 1, "V": 5, "X": 10,
                    "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        for key, val in sub_dict.items():
            result += (s.count(key) * val)
            s = s.replace(key, '')

        for key, val in add_dict.items():
            result += (s.count(key) * val)

        return result
