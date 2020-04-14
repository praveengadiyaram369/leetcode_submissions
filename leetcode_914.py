# _914. X of a Kind in a Deck of Cards


class Solution:

    def get_gcd_list(self, nums):
        gcd = math.gcd(nums[0], nums[1])
        for index in range(2, len(nums)):
            gcd = math.gcd(gcd, nums[index])

        return gcd

    def hasGroupsSizeX(self, deck) -> bool:

        if len(deck) < 2:
            return False

        values = list(collections.Counter(deck).values())
        min_value = min(values)

        if min_value < 2:
            return False
        elif len(values) == 1:
            return True

        common_freq = self.get_gcd_list(values)

        if common_freq == 1:
            return False

        for value in values:
            if value % common_freq != 0:
                return False
        return True
