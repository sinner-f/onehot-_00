class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_has_zero = [0 in row for row in matrix]#遍历 matrix 的每一行，判断这一行里有没有 0，得到一个布尔列表。
        col_has_zero = [0 in col for col in zip(*matrix)]#判断每一列是否包含 0。其中 zip(*matrix) 相当于把矩阵的“行”转换成“列”
        for i , row0 in enumerate(row_has_zero):
            for j , col0 in enumerate(col_has_zero):
                if row0 or col0:
                    matrix[i][j] = 0