class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        strings = s.split(' ')
        if len(p) != len(strings):
            return False
        word_map_f = {}
        word_map_b = {}
        for c, word in zip(p, strings):
            # print(c, word, word_map_f, word_map_b)
            if c in word_map_f and word_map_f[c] != word:
                return False
            if c in word_map_f and word_map_f[c] == word:
                continue
            if word in word_map_b and word_map_b[word] != c:
                return False
            if word in word_map_b and word_map_b[word] == c:
                continue
            word_map_f[c] = word
            word_map_b[word] = c
        return True

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    assert result == True