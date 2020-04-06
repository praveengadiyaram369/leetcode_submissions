# _1313. Decompress Run-Length Encoded List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        decompressed_data = []
        for index in range(int(len(nums)/2)):
            value = nums[(2 * index) + 1]
            decompressed_data.extend([value for i in range(nums[(2 * index)])])
        return decompressed_data