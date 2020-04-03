# _344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        for index in range(int(n/2)):
            temp = s[index]
            s[index] = s[n-index-1]
            s[n-index-1] = temp