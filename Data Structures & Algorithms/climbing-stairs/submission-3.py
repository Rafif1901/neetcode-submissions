class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n ==2: return 2
        second=count= 2
        first=1
        res= 0
        while count < n:
            res= first+second  
            first=second 
            second=res
            count+=1  
        return res