class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.powerset=[]
        def dfs(i,arr):
            if i>=len(nums):
                self.powerset.append(arr)
                return
            else:
                dfs(i+1,arr+[nums[i]])
                dfs(i+1,arr)
        arr=[]
        dfs(0,arr)
        return self.powerset
        