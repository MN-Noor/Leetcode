class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        ans=[0]
        size=1
        while size<=n:
            length=len(ans)
            for i in range(length):
                ans.append(ans[i]+1)
                size+=1  
                if size>=n+1:
                    break         
        return ans
        


            

      


        