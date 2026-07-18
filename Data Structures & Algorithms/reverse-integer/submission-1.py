class Solution:
    def reverse(self, x: int) -> int:
        min_t, max_t = -2**31, 2**31
        #reversed_x = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        s = str(x)
        if x < 0:
            reversed_x = s[1:][::-1]
            ans = -(int(reversed_x))
        else:
            reversed_x = s[::-1]
            ans = int(reversed_x)

        #if reversed_x < min_t or reversed_x > max_t:
        #    return 0
        if ans < min_t or ans > max_t:
            return 0
        return ans

        