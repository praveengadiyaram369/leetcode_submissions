# _1365. How Many Numbers Are Smaller Than the Current Number


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        num_cnt = 0
        prev = sorted_nums[0]
        nums_dict = {prev: num_cnt}

        for index in range(1, len(sorted_nums)):
            num_cnt += 1
            if sorted_nums[index] != prev:
                prev = sorted_nums[index]
                nums_dict[prev] = num_cnt

        result = []
        for value in nums:
            result.append(nums_dict[value])

        return result
