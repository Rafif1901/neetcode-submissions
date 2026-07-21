class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        seen = []
        total_length = 0 
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.append(s[r])
            total_length = max(total_length, r-l+1)
        return total_length