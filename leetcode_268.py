# _268. Missing Number


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        xor = 0
        for idx in range(len(nums)):
            xor ^= ((idx+1) ^ nums[idx])

        return xor


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return int(len(nums)*(len(nums)+1)/2) - sum(nums)
