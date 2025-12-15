class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        print(self.computeMatrix(matrix))

    def computeMatrix(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                left = matrix[i][j-1] if j > 0 else 0
                up=matrix[i-1][j] if i>0 else 0
                upleft=matrix[i-1][j-1] if i>0 and j>0 else 0
                matrix[i][j]=matrix[i][j]+left+up-upleft
        return matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left=self.matrix[row2][col1-1] if col1>0 else 0 
        up=self.matrix[row1-1][col2] if row1>0 else 0
        upleft=self.matrix[row1-1][col1-1] if row1>0 and col1>0 else 0
        sumofR=self.matrix[row2][col2]-left-(up-upleft)
        return sumofR




        
        



        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)