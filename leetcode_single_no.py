# _Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        xor_value = nums[0]
        for index in range(1, len(nums)):
            xor_value ^= nums[index]
        
        return xor_value