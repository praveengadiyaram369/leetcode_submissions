# _448. Find All Numbers Disappeared in an Array

# _array replace solution


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for idx in range(len(nums)):

            while nums[idx] != (idx+1) and (nums[idx] != nums[nums[idx] - 1]):
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]

        result = []

        for idx in range(len(nums)):
            if idx+1 != nums[idx]:
                result.append(idx+1)

        return result

# _markers solution


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for idx in range(len(nums)):

            if nums[abs(nums[idx]) - 1] > 0:
                nums[abs(nums[idx]) - 1] *= -1

        result = []

        for idx in range(len(nums)):
            if nums[idx] > 0:
                result.append(idx+1)

        return result
