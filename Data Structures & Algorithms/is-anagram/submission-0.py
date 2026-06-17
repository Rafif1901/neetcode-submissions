class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq_map_s = {}
        freq_map_t = {}

        for i, char1 in enumerate(s):
            freq_map_s[char1] = freq_map_s.get(char1, 0) + 1

        for j, char2 in enumerate(t):
            freq_map_t[char2] = freq_map_t.get(char2, 0) + 1

        if freq_map_s == freq_map_t:
            return True
         
        return False

