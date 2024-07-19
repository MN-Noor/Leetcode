class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        for i in range(l):
            print(nums[nums[i]])
            nums[i]=nums[i]+(nums[nums[i]]%l*l)
        for i in range(l):
            nums[i]=nums[i]//l
        return nums