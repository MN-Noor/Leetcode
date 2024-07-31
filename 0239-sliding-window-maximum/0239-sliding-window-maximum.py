from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()
        res=[]
        l=0
        for i in range(len(nums)):
            while d and nums[d[-1]]<=nums[i]:
                d.pop()
            d.append(i)

            if d[0]==i-k:
                d.popleft()
            if i>=k-1:
                res.append(nums[d[0]])

        return res



        
        