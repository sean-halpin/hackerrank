def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    s_chars = {}
    t_chars = {}
    for i in range(len(s)):
        s_chars[s[i]] = 1 + s_chars.get(s[i], 0)
        t_chars[t[i]] = 1 + t_chars.get(t[i], 0)
    for c in s_chars:
        if s_chars[c] != t_chars.get(c, 0):
            return False
    return True
        
        

print(valid_anagram("anagram", "nagaram"))
    
# Q: How to solve without using extra memory?
# Ans: If we sort both strings & compare for equality

def valid_anagram_o_1_mem(s, t):
    return sorted(s) == sorted(t)