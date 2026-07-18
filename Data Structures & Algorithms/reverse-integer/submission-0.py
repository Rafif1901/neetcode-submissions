class Solution:
    def reverse(self, x: int) -> int:
        min_t, max_t = -2**31, 2**31
        reversed_x = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        if reversed_x < min_t or reversed_x > max_t:
            return 0
        return reversed_x

        