class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        b = len(matrix)
        for row in range(b):
            for column in range(row+1,b):
                matrix[row][column], matrix[column][row]= matrix[column][row], matrix[row][column]
        for row in matrix:
            row.reverse()
        return matrix


        