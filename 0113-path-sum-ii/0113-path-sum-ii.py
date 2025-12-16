# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root ==None:
            return []
        else:
            res=[]
            self.findPath(targetSum,0,res,[],root)
            return res
    def findPath(self,targetSum , sum, marray ,arr,root):
        if root ==None:return marray
        sum+=root.val
        arr.append(root.val)
        if root.left==None and root.right==None:
            if sum==targetSum:
                marray.append(arr.copy())
        else:
            self.findPath(targetSum,sum,marray,arr,root.left)
            self.findPath(targetSum,sum,marray,arr,root.right)
        arr.pop()
            
    
        
        