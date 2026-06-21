class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        
        for c in strs:
            key = tuple(sorted(c))

            if key not in map:
                map[key] = [c]
            
            else:
                map[key].append(c)
        
        return list(map.values())