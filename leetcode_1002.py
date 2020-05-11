# _1002. Find Common Characters


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        char_dict = {}
        for char in A[0]:
            if char not in char_dict.keys():
                char_dict[char] = 1
            char_dict[char] += 1

        for word in A:
            for char in char_dict.keys():
                char_dict[char] = min(char_dict[char], word.count(char))

        result = []
        for char, cnt in char_dict.items():
            while cnt > 0:
                result.append(char)
                cnt -= 1
        return result
