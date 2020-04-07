# _1299. Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1:
            return [-1]
        
        n = len(arr)
        max_list = [0] * n
        max_value = arr[n-1]
        
        max_list[n-1] = -1
        max_list[n-2] = max_value
        
        for index in range(n-2, 0, -1):
            max_value = max(max_value, arr[index])
            max_list[index-1] = max_value
        
        return max_list