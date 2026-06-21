class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #map = {}
        
        #for c in strs:
        #    key = tuple(sorted(c))

        #    if key not in map:
        #        map[key] = [c]
            
        #    else:
        #        map[key].append(c)
        
        #return list(map.values())

        map = defaultdict(list)

        for c in strs:
            key = [0] * 26
            for x in c:
                key[ord(x) - ord('a')] +=1

            key = tuple(key)
        
            map[key].append(c)
        return list(map.values())