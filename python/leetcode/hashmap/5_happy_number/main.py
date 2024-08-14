class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = {n: True}
        nums = [int(c) for c in list(str(n))]
        while True:
            sum = 0
            for num in nums:
                # print(sum, num, num**2)
                sum = sum + (num**2)
            # print(sum)
            if sum in seen:
                # print(sum, seen)
                return False
            elif sum == 1:
                return True
            else:
                seen[sum] = True
                nums = [int(c) for c in list(str(sum))]

if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))
    print(s.isHappy(7))
    print(s.isHappy(1111111))