def first_non_repeating_char(inp):
    seen = {}
    first = ""
    for c in inp[::-1]:
        if c not in seen:
            seen[c] = True
            first = c
        elif c == first:
            first = ""
    return None if first == "" else first

print( first_non_repeating_char('swiss') )
print( first_non_repeating_char('w') )
print( first_non_repeating_char("Bin") )
print( first_non_repeating_char('bin') )
print( first_non_repeating_char('leetcode') )
print( first_non_repeating_char('hello') )
print( first_non_repeating_char('aabbcc') )

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""