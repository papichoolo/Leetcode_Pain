# This is a bottom up approach, solving the subproblems first to balloon up to the larger problem at hand
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3,-1,-1):
            cost[i]= min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1])
# Time complexity: O(n)

#[10,15,20]0 (we add 0 in the end), then we basically check what is the minumum cost of the either jumping forward one step or jumping two steps