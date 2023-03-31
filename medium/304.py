from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[None for _ in range(n)] for _ in range(m)]
        self.dp[0][0] = matrix[0][0]
        # generate prefix
        # DP
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    self.dp[i][j] = self.dp[i][j - 1] + matrix[i][j]
                elif j == 0:
                    self.dp[i][j] = self.dp[i - 1][j] + matrix[i][j]
                else:
                    self.dp[i][j] = self.dp[i-1][j] + \
                        self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]

        # Recursive
        # def generate(row, col):
        #     if row < 0 or col < 0:
        #         return 0
        #     if self.dp[row][col] != None:
        #         return self.dp[row][col]
        #     self.dp[row][col] = generate(
        #         row - 1, col) + generate(row, col - 1) - generate(row - 1, col - 1) + matrix[row][col]
        #     return self.dp[row][col]
        # generate(m - 1, n - 1)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        if row1 == 0:
            return self.dp[row2][col1] - self.dp[row2][col1 - 1]
        if col1 == 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        return self.dp[row2][col2] \
            - self.dp[row1-1][col2] \
            - self.dp[row2][col1-1] \
            + self.dp[row1 - 1][col1 - 1]


a = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [
              4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
