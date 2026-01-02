class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash={}
        for i in range(len(nums)):
            if nums[i] in hash:
                return nums[i]
            else:
                hash[nums[i]]=i


        