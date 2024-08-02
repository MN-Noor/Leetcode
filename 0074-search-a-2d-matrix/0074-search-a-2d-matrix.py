class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow,ncol=len(matrix),len(matrix[0])
        top=0
        bottom=nrow-1
        while top<=bottom:
            row=(top+bottom)//2
            if target<matrix[row][0]:
                bottom=row-1
            elif target>matrix[row][-1]:
                top=row+1
            else:
                break

        if top>bottom:
            print("hello")
            return False

        l,r=0,ncol-1
        mid_row=(top+bottom)//2
        while l<=r:
            mid=(r+l)//2
            if matrix[mid_row][mid]<target:
                l=mid+1
              
            elif matrix[mid_row][mid]>target:
                r=mid-1
                
            else:
                return True
        return False
            
            