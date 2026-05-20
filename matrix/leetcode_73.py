class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_has_zero = [0 in row for row in matrix]
        col_has_zero = [0 in col for col in zip(*matrix)]
        for i , row0 in enumerate(row_has_zero):
            for j , col0 in enumerate(col_has_zero):
                if row0 or col0:
                    matrix[i][j] = 0