from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        total_candies = 1
        lpass, rpass = [1], [1]
        
        #right pass
        current_candies = 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                current_candies +=1
            else:
                current_candies = 1
            rpass.insert(0,current_candies)
        #left pass
        current_candies = 1
        for i in range(0, len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                current_candies +=1
            else:
                current_candies = 1
            lpass.append(current_candies)
        result = []
        for i in range(len(ratings)):
            result.append(max(lpass[i], rpass[i]))
        total_candies = sum(result)
        return total_candies
    
if __name__ == "__main__":
    sol = Solution()
    inp = [1,3,2,2,1]
    res = sol.candy(inp)
    print(res)
    assert res == 7