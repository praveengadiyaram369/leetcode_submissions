# _7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int: 
        if (x == 0):
            return 0
        
        x_abs = abs(x)
        while True:
            reminder = int(x_abs % 10)
            if reminder == 0:
                x_abs = int(x_abs / 10)
            else:
                break
                
        x_abs_str = list(str(x_abs))
        x_len = len(x_abs_str)
        for index in range(int(x_len/2)):
            temp = x_abs_str[index]
            x_abs_str[index] = x_abs_str[x_len - index - 1]
            x_abs_str[x_len - index - 1] = temp
        
        x_rev_str = ''
        for value in x_abs_str:
            x_rev_str += value
        
        x_reverse = int(x_rev_str)
        if x < 0:
            x_reverse = (-1 * x_reverse)
        
        if (x_reverse > 2147483647) or (x_reverse < -2147483648):
            return 0
        
        return x_reverse