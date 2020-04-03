# _1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_sorted = sorted(nums)
        lower = 0
        upper = len(nums_sorted)-1 
        
        while lower < upper:
            
            curr_sum = nums_sorted[lower] + nums_sorted[upper]
            
            if curr_sum > target:
                upper -= 1
            elif curr_sum < target:
                lower += 1
            elif curr_sum == target:
                if nums_sorted[lower] != nums_sorted[upper]:
                    lower = nums.index(nums_sorted[lower])
                    upper = nums.index(nums_sorted[upper])
                    return [lower, upper]
                else:
                    return [i for i, x in enumerate(nums) if x == nums_sorted[upper]]