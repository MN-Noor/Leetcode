# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        node1=head
        power=self.find_length(head)-1
        print(power)
        decimal=0
        while node1!=None and power>=0:
            if node1.val==1:
                decimal+=2**power
            power-=1
            node1=node1.next
        return decimal
    def find_length(self,head):
        len=0
        while head!=None:
            head=head.next
            len+=1
        return len
