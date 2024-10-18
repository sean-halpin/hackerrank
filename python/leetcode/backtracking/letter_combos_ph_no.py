from typing import List


nmap = {
    '2':"abc",
    '3':"def",
    '4':"ghi",
    '5':"jkl",
    '6':"mno",
    '7':"pqrs",
    '8':"tuv",
    '9':"wxyz"
}

class Solution:
    def lettersBackTrack(curr, remain) -> List[str]:
        res = []
        if curr is '':
            return res
        chars = nmap[curr]
        for c in chars:
            if remain is not '':
                tail = Solution.lettersBackTrack(remain[0], remain[1:])
                for t in tail:
                    res.append(c+t)
            else:
                res.append(c)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        if digits is '':
            return []
        return Solution.lettersBackTrack(digits[0], digits[1:])


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations('23'))
    print(sol.letterCombinations('234'))
    print(sol.letterCombinations(''))
    print(sol.letterCombinations('2'))
    print(sol.letterCombinations('3'))
    print(sol.letterCombinations('4'))
    print(sol.letterCombinations('5'))
    print(sol.letterCombinations('6'))
    print(sol.letterCombinations('7'))
    print(sol.letterCombinations('8'))
    print(sol.letterCombinations('9'))
    print(sol.letterCombinations('23456789'))