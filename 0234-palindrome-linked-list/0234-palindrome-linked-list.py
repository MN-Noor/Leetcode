# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        midpoint=self.findMid(head)
        reversedList=self.reverseList(midpoint)
        self.printLinked(reversedList)
        print("head")
        self.printLinked(head)
        while reversedList!=None:
            if head.val!=reversedList.val:
                return False
            head=head.next
            reversedList=reversedList.next
        return True

    def findMid(self,head):
        fast=head
        slow=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
    def reverseList(self,node):
        prev=None
        current=node
        while current!=None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev
    def printLinked(self,node):
        while node!=None:
            print(node.val)
            node=node.next
                
        
            

