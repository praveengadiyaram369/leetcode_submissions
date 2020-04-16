# _840. Magic Squares In Grid


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        grid_cnt = 0

        if m < 3 or n < 3:
            return 0

        row_xor = 0
        for num in range(1, 10):
            row_xor ^= num

        for i in range(m-2):
            for j in range(n-2):

                if grid[i+1][j+1] == 5:
                    num_1 = grid[i][j]
                    num_2 = grid[i][j+1]
                    num_3 = grid[i][j+2]
                    num_4 = grid[i+1][j]
                    num_5 = grid[i+1][j+1]
                    num_6 = grid[i+1][j+2]
                    num_7 = grid[i+2][j]
                    num_8 = grid[i+2][j+1]
                    num_9 = grid[i+2][j+2]

                    final_xor = (row_xor ^ num_1 ^ num_2 ^ num_3 ^
                                 num_4 ^ num_5 ^ num_6 ^ num_7 ^ num_8 ^ num_9)

                    if final_xor == 0 and (num_1 + num_2 + num_3 == num_4 + num_5 + num_6 == num_7 + num_8 + num_9 == num_1 + num_4 + num_7 == num_2 + num_5 + num_8 == num_3 + num_6 + num_9 == num_1 + num_5 + num_9 == num_3 + num_5 + num_7):
                        grid_cnt += 1

        return grid_cnt
