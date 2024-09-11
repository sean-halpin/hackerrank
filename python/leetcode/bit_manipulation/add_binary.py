class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # ba = int(a, 2)
        # bb = int(b, 2)
        # return bin(ba + bb)[2:]
        
        la = len(a)
        lb = len(b)
        i = la -1
        j = lb -1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res.append(str(carry % 2))
            carry = carry // 2
            # print(i, j, carry)

        return "".join(res[::-1])
