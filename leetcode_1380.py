# _1380. Lucky Numbers in a Matrix

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        row_list = [min(row) for row in matrix]
        col_list = [max([row[col] for row in matrix]) for col in range(len(matrix[0]))]
        
        return [value for value in row_list if value in col_list]