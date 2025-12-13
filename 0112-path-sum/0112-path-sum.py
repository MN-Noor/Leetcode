# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:return False
        else:
            return self.findSum(root,0,targetSum)
        
    def findSum(self,root,sum,target):
        if not root:
            return False
        if not root.left and not root.right:
            sum=sum + root.val
            if sum==target:
                return True
        else:
            sum=sum+root.val
        return self.findSum(root.left,sum,target) or self.findSum(root.right,sum,target)
            
        