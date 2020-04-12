# _532. K-diff Pairs in an Array


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if len(nums) < 2:
            return 0

        nums.sort()

        diff_pair_list = []
        l = 0
        r = 1

        while r < len(nums):
            diff = abs(nums[r] - nums[l])
            if diff == k:
                if (nums[r], nums[l]) not in diff_pair_list:
                    diff_pair_list.append((nums[r], nums[l]))
                l += 1
                r += 1
            elif diff < k:
                r += 1
            elif diff > k and r > l+1:
                l += 1
            else:
                l += 1
                r += 1

        return len(diff_pair_list)
