class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            if (s[i] in map_s and map_s[s[i]] != t[i]) or (t[i] in map_t and map_t[t[i]] != s[i]):
                return False
            if s[i] not in map_s:
                map_s[s[i]] = t[i]
            if t[i] not in map_t:    
                map_t[t[i]] = s[i]
        return True
