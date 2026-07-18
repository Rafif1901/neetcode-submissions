class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2

        first, second =0, 1
        for i in range(n):
            res = first + second
            first, second = second, res
        return res