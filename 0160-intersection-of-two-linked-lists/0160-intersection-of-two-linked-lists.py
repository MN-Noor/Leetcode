# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#brute force approach
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         slow=headA
#         while slow!=None:
#             fast=headB
#             while fast!=None:
#                 if fast==slow:
#                     return fast
#                 fast=fast.next
#             slow=slow.next
#         return None
#Hashing Approach
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        store=headA
        search=headB
        hashset=set()
        while store!=None:
            hashset.add(store)
            store=store.next

        while search!=None:
            if search in hashset:
                return search
            search=search.next
        return None

        