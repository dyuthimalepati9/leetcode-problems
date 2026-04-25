class Solution: 
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
            row, col =   len(matrix)-1, 0        
            while row >=0 and col <= len(matrix[0])-1:  
                cell = matrix[row][col]
                if cell > target:    row-= 1   
                elif cell < target:  col+= 1    
                else: return True               
            return  False 