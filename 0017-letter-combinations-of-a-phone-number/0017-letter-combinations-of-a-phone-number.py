class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr=[]
        for d in digits:
            arr.append(self.getLetter(int(d)))
        def dfs(s,i,j,ans):
            if i>=len(arr):
                ans.append(s)
                return ans
            else:
                for j in range(len(arr[i])):
                    dfs(s+arr[i][j],i+1,0,ans)
            return ans
            
        return dfs("",0,0,[])
    def getLetter(self, digit: int) -> List[str]:
        if digit <= 6:
            start = (digit - 1) * 3 - 2
            count = 3

        elif digit == 7:
            start = 16   # p
            count = 4

        elif digit == 8:
            start = 20   # t
            count = 3

        else:  # 9
            start = 23   # w
            count = 4

        return [chr(96 + start + i) for i in range(count)]