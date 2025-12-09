class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)
        for i in range(n+1):
            res[i]=self.count(i)
        return res

    def count(self,i):
        count=0
        while i!=0:
            count+=i & 1
            i=i>>1
        return count


        