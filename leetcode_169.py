# _169. Majority Element

# _haspmap solution


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maj = 0
        maj_cnt = 0
        num_dict = {}

        for val in nums:

            if val not in num_dict.keys():
                num_dict[val] = 1
            else:
                num_dict[val] += 1

            if num_dict[val] > maj_cnt:
                maj_cnt = num_dict[val]
                maj = val

        return maj

# _Boyer-Moore majority voting algorithm


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maj_cnt = 1
        maj = nums[0]

        for idx in range(1, len(nums)):
            if maj_cnt == 0:
                maj = nums[idx]
                maj_cnt = 1
            elif maj == nums[idx]:
                maj_cnt += 1
            else:
                maj_cnt -= 1

        return maj
