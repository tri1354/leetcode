class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for k in range(row):
            matrix[k].reverse()


        # first = 0
        # last = len(matrix) - 1
        # n = last
        # while first < last:
        #     for i in range(first, last):
        #         matrix[first][i], matrix[i][last] = matrix[i][last], matrix[first][i]
        #         matrix[first][i], matrix[n - i][first] = matrix[n - i][first], matrix[first][i]
        #         matrix[n - i][first], matrix[last][n - i] = matrix[last][n - i], matrix[n - i][first]
        #     first += 1
        #     last -= 1