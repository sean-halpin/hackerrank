class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        int_sum = 0
        i = len(s)-1
        while i >= 0:
            curr = mapping[s[i]]
            if i > 0:
                prev = mapping[s[i-1]]
                if prev < curr:
                    curr = curr - prev
                    i-=1
            int_sum += curr
            i-=1
        return int_sum

sol = Solution()
rom = "MCMXCIV"
expected = 1994
res = sol.romanToInt(rom)
assert res == expected
print(rom, "to", res)