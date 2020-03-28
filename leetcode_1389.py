# _1389. Create Target Array in the Given Order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        else:
            target_list = []
            for num, ind in zip(nums, index):
                target_list.append(num)
                
                upper_bound = len(target_list) - 1
                lower_bound = ind
                
                while upper_bound - lower_bound > 0:
                    
                    swap_value = target_list[upper_bound]
                    target_list[upper_bound] = target_list[upper_bound - 1]
                    target_list[upper_bound - 1] = swap_value
                    upper_bound -= 1
                    
            return target_list