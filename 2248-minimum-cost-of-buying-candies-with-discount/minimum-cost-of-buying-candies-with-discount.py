class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        i = n - 1
        total_cost = 0

        while i >= 0:
            total_cost += cost[i]  

            if i - 1 >= 0:
                total_cost += cost[i - 1] 
            i -= 3

        return total_cost