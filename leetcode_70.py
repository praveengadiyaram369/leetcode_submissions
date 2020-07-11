# _70. Climbing Stairs

# _brute force approach
class Solution:

    def factorial(self, a):
        if a == 0 or a == 1:
            return 1

        return a * self.factorial(a - 1)

    def getStepCount(self, a, b):
        return self.factorial(a+b)/(self.factorial(a) * self.factorial(b))

    def climbStairs(self, n: int) -> int:

        one_cnt = n
        two_cnt = 0
        step_cnt = 0

        for cnt in range(n):
            step_cnt += int(self.getStepCount(one_cnt, two_cnt))
            one_cnt -= 2
            two_cnt += 1

            if one_cnt < 0:
                return step_cnt


# _dynamic programming
class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        a = 1
        b = 2
        
        for val in range(n-2):
            a , b = b, a+b
        
        return b