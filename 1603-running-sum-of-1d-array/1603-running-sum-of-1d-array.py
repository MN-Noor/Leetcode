class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        sum_num=0
        for i in nums:
            sum_num+=i
            result.append(sum_num)
        return result

        