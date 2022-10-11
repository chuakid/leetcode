class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        ans = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        # first pass
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i-1][j] + 1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j-1] + 1)

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i < rows - 1:
                    ans[i][j] = min(ans[i][j], ans[i+1][j] + 1)
                if j < cols - 1:
                    ans[i][j] = min(ans[i][j], ans[i][j+1] + 1)
        return ans
