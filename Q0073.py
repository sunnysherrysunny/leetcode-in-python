from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowToSet = set()
        colToSet = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col] == 0):
                    rowToSet.add(row)
                    colToSet.add(col)
        

        for row in rowToSet:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        for col in colToSet:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        
            

m = [[]]
s = Solution()
s.setZeroes(m)
print(m)
