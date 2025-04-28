class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=hashmap.get(nums[i],0)+1 
        good=0
        for key,value in hashmap.items():
            if value> 1:
                good+=value*(value-1)//2
        return good
