# leetcode url: https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        elems = s.split(" ")[::-1]
        res = []
        for e in elems:
            # print(f'e:{e}-FIN')
            if e == "":
                continue
            else:
                res.append(e)
        return (" ".join(res)).strip()


