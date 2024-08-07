class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,num in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<num:
                index=stack.pop()
                res[index]=i-index
            stack.append(i)
        
        return res






        