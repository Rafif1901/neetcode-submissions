class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            output = (output << 1) | (1&n)
            n = n >> 1
        return output