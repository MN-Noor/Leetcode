import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            mid=(l+r)//2
            n_bna=0
            for i in piles:
                n_bna=n_bna+(math.ceil(i/mid))
            if n_bna<=h:
                r=mid-1
            elif n_bna>h:
                l=mid+1
        
        return l


            


        