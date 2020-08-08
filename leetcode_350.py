# _350. Intersection of Two Arrays II


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 == 0 or n2 == 0:
            return []

        nums1.sort()
        nums2.sort()

        p1 = p2 = 0
        result = []
        while p1 < n1 and p2 < n2:

            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        return result
