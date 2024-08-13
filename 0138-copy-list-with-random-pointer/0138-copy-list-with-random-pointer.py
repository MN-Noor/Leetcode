"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        hash={None:None}
        
        while curr != None:
            newNode=Node(curr.val)
            hash[curr]=newNode
            curr=curr.next
        curr=head
        while curr!=None:
            newNode=hash[curr]
            newNode.next=hash[curr.next]
            newNode.random=hash[curr.random]
            curr=curr.next
        return hash[head]