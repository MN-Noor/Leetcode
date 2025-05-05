# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpt=head
        fastpt=head
        while slowpt!=None and fastpt!=None and fastpt.next!=None:
            slowpt=slowpt.next
            fastpt=fastpt.next.next
            if fastpt==slowpt:
                return True
        return False
        

    
