# _1295. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for item in nums:
            if len(str(item)) % 2 == 0:
                even_count += 1
        return even_count 