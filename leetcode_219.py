class Solution:
    
    def check_for_k_duplicate(self, data, k):
        
        l = 0
        r = 1
        while l < r and r < len(data):
            diff = data[r] - data[l]
            if diff <= k:
                return True
            else:
                l += 1
                if l == r:
                    r += 1
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) < 2:
            return False
        
        nums_dict = {}
        for index, value in enumerate(nums):
            if value not in nums_dict.keys():
                tmp = [index]
                nums_dict[value] = tmp
                       
            nums_dict[value].append(index)
            
        for key, value in nums_dict.items():
            if len(value) > 1 and self.check_for_k_duplicate(value, k) is True:
                return True
        
        return False
