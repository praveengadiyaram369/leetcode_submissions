# _26. Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = r = 0
        n = len(nums)
        while r < n:
            if nums[l] == nums[r]:

                while r < n and nums[r] == nums[l]:
                    r += 1

                if r < n:
                    l += 1
                    nums[l] = nums[r]
        return l+1
