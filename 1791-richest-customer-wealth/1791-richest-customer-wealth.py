class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for i in accounts:
            total_wealth=0
            for j in i:
                total_wealth+=j
            if max_wealth <=total_wealth:
                max_wealth=total_wealth
        return max_wealth

        