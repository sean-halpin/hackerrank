def solution(S):
    stack = []
    valid = "(){}[]"
    opening = "{[("
    closing = "}])"
    inverse = {
        "{":"}",
        "(":")",
        "[":"]",
        "}":"{",
        ")":"(",
        "]":"[",
    }
    only_closing = False
    for c in S: 
        if c in valid:
            if c in opening:
                if only_closing: 
                    return 0
                stack.append(c)
            elif c in closing:
                if stack and inverse[c] == stack[-1]:
                    stack.pop()
                else:
                    return 0
        else:
            only_closing = True
    return 1 if not stack else 0