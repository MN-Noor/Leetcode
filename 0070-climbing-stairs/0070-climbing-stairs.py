class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo={}
        
        def dfs(n):
            if n==0:
                return 1
            elif n<0:
                return 0
            else:
                if n not in self.memo:
                    self.memo[n]= (dfs(n-1)+dfs(n-2))
                return self.memo[n]
        return dfs(n)
        
        
            
        