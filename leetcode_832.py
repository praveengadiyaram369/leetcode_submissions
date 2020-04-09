# _832. Flipping an Image

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        m = len(A)
        n = len(A[0])
        col_size = floor(n/2)
        
        if m == 1 and n == 1:
            if A[0][0] == 0:
                A[0][0] = 1
            else:
                 A[0][0] = 0
            
            return A
        
        for i in range(m):
                   
            if n % 2 != 0:
                if A[i][col_size] == 0:
                    A[i][col_size] = 1
                else:
                    A[i][col_size] = 0

                    
            for j in range(col_size):
                
                
                col = n-j-1
                    
                if A[i][j] == 0 and A[i][col] == 0:
                    A[i][j] = 1
                    A[i][col] = 1
                elif A[i][j] == 1 and A[i][col] == 1:
                    A[i][j] = 0
                    A[i][col] = 0
        
        return A





# _2nd approach from solution provided

        for row in A:
            for i in range(int((len(row) + 1)/2)):
                
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1  ## a, b = b, a
                                                            ## row[~i] = row[len(row) -i -1]
                                                            ## AND (^) 1, to reverse binary data
                
        return A