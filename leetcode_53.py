# _53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        curr_sum = nums[0]
        for index in range(1, len(nums)):
            curr_sum += nums[index]
            curr_sum = max(curr_sum, nums[index])
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum