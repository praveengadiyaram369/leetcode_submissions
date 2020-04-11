

# _Approach 1 using sorting and taking extra space
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        sorted_nums = sorted(nums)
        lower = None
        upper = None
        
        for index in range(len(nums)):
            if nums[index] != sorted_nums[index]:
                lower = index
                break
        
        for index in range(len(nums)-1, 0, -1):
            if nums[index] != sorted_nums[index]:
                upper = index
                break
        
        if lower is not None and upper is not None:
            return (upper - lower + 1)
        else:
            return 0


# Approach 2

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        flag = False
        min_value = 10001
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                flag = True
            if flag is True:
                min_value = min(min_value, nums[i+1])
                
        max_value = -10001
        flag = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                flag = True
            if flag is True:
                max_value = max(max_value, nums[i-1])
        

        l = 0
        r = 0
        for i in range(len(nums)):
            if min_value < nums[i]:
                l = i
                break
                
        for i in range(len(nums)-1, 0, -1):
            if max_value > nums[i]:
                r = i
                break
        
        if r-l <= 0:
            return 0
        else:
            return r-l+1