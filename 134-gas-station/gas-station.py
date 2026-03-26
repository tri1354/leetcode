class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        i = 0
        check = 0
        car_gas = gas[i]
        while i < len(gas)-1:
            car_gas -= cost[i]
            i += 1
            if car_gas >= 0:
                car_gas += gas[i]
            else:
                car_gas = gas[i]
                check = i
        return check