# _1304. Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        zero_list = []
        if n % 2 != 0:
            zero_list.append(0)
            n -= 1
        
        for value in range(1, int(n/2) + 1):
            zero_list.append(value)
            zero_list.append((-1 * value))
        
        return zero_list