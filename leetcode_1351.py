# _1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m = len(grid)-1
        n = len(grid[0])-1
        negative_cnt = 0
        
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                
                if grid[j][i] < 0:
                    negative_cnt += 1
                else:
                    break
        
        return negative_cnt