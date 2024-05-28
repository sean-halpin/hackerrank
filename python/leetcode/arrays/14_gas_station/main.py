from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        start = 0
        fuel = 0
        print("start:", start)
        for i in range(n):
            print(i)
            fuel = fuel + gas[i] - cost[i]
            if fuel < 0:
                print("start:", start)
                start = i + 1
                fuel = 0
        return start

if __name__ == "__main__":   
    nums = [1, 2, 3, 4]
    solution = Solution()
    output = solution.canCompleteCircuit(nums, nums)
    print(output)
    assert output == 0