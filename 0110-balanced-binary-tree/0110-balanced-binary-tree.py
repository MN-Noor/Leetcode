# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       isBalanced,Height=self.findHeight(root)
       return isBalanced
            
    
    def findHeight(self,root):
        if not root:return True,0
        else:
            isBalancedLeft,left=self.findHeight(root.left)
            isBalancedRight,right=self.findHeight(root.right)
            height=max(left,right)+1
            if abs(left-right)>1 or not isBalancedLeft or not isBalancedRight :
                return False,height
            else:
                return True,height

        