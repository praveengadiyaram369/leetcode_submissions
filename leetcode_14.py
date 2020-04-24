# _14. Longest Common Prefix

class Solution:
    
    def get_common_prefix(self, a, b):
        l = 0
        while l<len(a) and l<len(b):
            if a[l] == b[l]:
                l += 1
            else:
                break
        return a[:l]
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        
        common_prefix = self.get_common_prefix(strs[0], strs[1])
        if common_prefix == '':
            return common_prefix
                
        for i in range(2, len(strs)):
            common_prefix = self.get_common_prefix(common_prefix, strs[i])
            
        return common_prefix