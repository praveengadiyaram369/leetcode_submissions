# _20. Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:

        data_dict = {'{': '}', '(': ')', '[': ']'}
        stack_data = []

        for value in s:
            if value in data_dict.keys():
                stack_data.append(value)
            elif len(stack_data) == 0 or value != data_dict[stack_data.pop()]:
                return False

        if len(stack_data) == 0:
            return True
        return False
