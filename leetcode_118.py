# _118. Pascal's Triangle


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []

        if numRows == 0:
            return result

        r = 2
        pascal = [1]
        result.append(pascal)

        while r <= numRows:
            pascal_old = pascal
            pascal = [1]

            for i in range(r-2):
                pascal.append(pascal_old[i] + pascal_old[i+1])

            pascal.append(1)
            result.append(pascal)
            r += 1

        return result
