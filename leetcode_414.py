# _414. Third Maximum Number

class Solution:
    
    def computemax(self, first_max, second_max, third_max, value_1):
        
        if value_1 != first_max and value_1 != second_max and value_1 != third_max:
            if value_1 > first_max:
                third_max, second_max, first_max = second_max, first_max, value_1
            elif value_1 > second_max:
                third_max, second_max = second_max, value_1
            elif value_1 > third_max:
                third_max = value_1
            
        return first_max, second_max, third_max
                    
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(set(nums)) < 3:
            return max(nums)
        
        first_max = nums[0]
        second_max = float("-inf")
        third_max = float("-inf")
        
        for index in range(int((len(nums)+1)/2)):                      
            first_max, second_max, third_max = self.computemax(first_max, second_max, third_max, nums[index])
            first_max, second_max, third_max = self.computemax(first_max, second_max, third_max, nums[~index])
            
        return third_max