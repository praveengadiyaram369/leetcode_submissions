# _189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%len(nums)

        # _solution 1
        # nums_updated = nums[(n-k):n]
        # nums_updated.extend(nums[0:(n-k)])
        # for index, value in enumerate(nums_updated):
        #     nums[index] = value
        
        # _solution 2
        # buffer = [value for value in nums]
        # for index, value in enumerate(buffer):
        #     nums[(index+k) % n] = value
        
        # _solution 3
        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp