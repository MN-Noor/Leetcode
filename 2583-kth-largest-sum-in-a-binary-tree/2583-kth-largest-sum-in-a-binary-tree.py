# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import heapq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=deque()
        list_sum=[]
        heap=[]
        if root==None:
            return -1
        q.append(root)
        while q:
            size=len(q)
            sum=0
            for i in range(size):
                elem=q.popleft()
                sum+=elem.val
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            if len(heap)<k:
                heapq.heappush(heap,sum)
            else:
                if heap[0]<sum:
                    heapq.heapreplace(heap,sum)
        return heap[0] if len(heap)==k else -1
        
            
            



            
            


        