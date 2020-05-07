# _283. Move Zeroes


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        n = len(nums)

        while r < n:
            if nums[l] == 0:
                while r < n and nums[r] == 0:
                    r += 1

                if r < n:
                    nums[l] = nums[r]
                    nums[r] = 0

            l += 1
            r += 1
