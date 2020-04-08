# _217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        value_dict = {}
        for value in nums:
            if value not in value_dict.keys():
                value_dict[value] = 1
            else:
                return True
        return False    