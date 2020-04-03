# _485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        consecutive_sum = 0
        max_sum = 0
        for value in nums:
            if value == 0 and consecutive_sum > max_sum:
                max_sum = consecutive_sum
                consecutive_sum = 0
            elif value == 0 and consecutive_sum <= max_sum:
                consecutive_sum = 0
            elif value == 1:
                consecutive_sum += 1
                
        if consecutive_sum > max_sum:
            max_sum = consecutive_sum
                
        return max_sum