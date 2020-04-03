# _1266. Minimum Time Visiting All Points

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        distance_sum = 0
        for index in range(len(points) - 1):
            distance_sum += max(abs(points[index][0] - points[index+1][0]), abs(points[index][1] - points[index+1][1]))
        
        return distance_sum