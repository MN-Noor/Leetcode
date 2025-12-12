# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s=0
        if root==None:
            return 0
        else:
            return self.leftSum(s,1,root)
        
    def leftSum(self,s,flag,root):
        if root==None:
            return 0
        if not root.left and not root.right:
            if flag==0:
                return root.val
            else:
                return 0
        return self.leftSum(s,0,root.left)+self.leftSum(s,1,root.right)
            




        


           

        