class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # i = 0
        # start = 0
        # car_gas = gas[i]
        # while i < len(gas)-1:
        #     car_gas -= cost[i]
        #     i += 1
        #     if car_gas >= 0:
        #         car_gas += gas[i]
        #     else:
        #         car_gas = gas[i]
        #         start = i
        # return start


        start = 0
        tank = 0
        for i, c in enumerate(cost):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start