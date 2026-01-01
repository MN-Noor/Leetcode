class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_index=(len(digits))-1
        if digits[last_index]<9:
            digits[last_index]=digits[last_index]+1
        else:
            while digits[last_index]==9:
                digits[last_index]=0
                last_index=last_index-1
            if last_index>=0:
                digits[last_index]=digits[last_index]+1
            else:
                digits.insert(0,1)
        return digits
        