class Solution(object):
    def combinationSum(self, candidates, target):
       ans=[]
       self.getAllCombinations(ans, [], 0, candidates, target)
       return ans
    def getAllCombinations(self,ans,combin,index,candidates,target):
        if index==len(candidates) or target<0:
            return
        if target==0:
            ans.append(list(combin))
            return

        combin.append(candidates[index])
        # # single
        # self.getAllCombinations(ans,combin,index+1,candidates,target-candidates[index])
        # multiple
        self.getAllCombinations(ans,combin,index,candidates,target-candidates[index])
        combin.pop()
        # exclusion
        self.getAllCombinations(ans,combin,index+1,candidates,target)


    