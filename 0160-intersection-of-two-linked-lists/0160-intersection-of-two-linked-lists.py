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
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         store=headA
#         search=headB
#         hashset=set()
#         while store!=None:
#             hashset.add(store)
#             store=store.next

#         while search!=None:
#             if search in hashset:
#                 return search
#             search=search.next
#         return None
#Difference Approach
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         sizeA=self.find_length(headA)
#         sizeB=self.find_length(headB)
#         longer=headA if sizeA>sizeB else headB
#         smaller=headA if sizeA<=sizeB else headB
#         diff=abs(sizeA-sizeB)
#         for i in range(diff):
#             longer=longer.next
#         while smaller!=None:
#             if smaller==longer:
#                 return smaller
#             else:
#                 smaller=smaller.next
#                 longer=longer.next       
#     def find_length(self,node):
#         size=0
#         while node!=None:
#             node=node.next
#             size+=1
#         return size

#swappingList Approach
class Solution:
     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        iterA=headA
        iterB=headB
        while iterA!=iterB:
            iterA=iterA.next if iterA else headB
            iterB=iterB.next if iterB else headA            
        return iterA

