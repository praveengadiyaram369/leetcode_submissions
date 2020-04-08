# _665. Non-decreasing Array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        modify_cnt = 0
        
        for index in range(len(nums)-1):
            
            if nums[index] > nums[index+1]:
                modify_cnt += 1
                if modify_cnt > 1:
                        return False
                    
                if index > 0:
                    if nums[index+1] <= nums[index-1]:
                        nums[index+1] = nums[index]   
        return True