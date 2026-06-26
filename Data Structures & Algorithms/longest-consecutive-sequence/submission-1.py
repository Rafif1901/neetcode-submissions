class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for n in sett:
            if n-1 not in sett:
                y = n+1
                while y in sett:
                    y+=1
                longest = max(longest, y-n)
        return longest