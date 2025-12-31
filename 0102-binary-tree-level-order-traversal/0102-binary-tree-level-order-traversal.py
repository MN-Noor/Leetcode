from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root==None:
            return res
        q=Queue()
        q.put(root)
        
        while not q.empty():
            s=q.qsize()
            arr=[]
            for i in range(s):
                node=q.get()
                if node.left:q.put(node.left)
                if node.right:q.put(node.right)
                arr.append(node.val)
            res.append(arr)
        return res



        