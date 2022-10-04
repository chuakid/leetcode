class Solution:
    def convert(self, s: str, numRows: int) -> str:
        newS = ""
        for row in range(numRows):
            down = row != numRows - 1
            currChar = row
            while currChar < len(s):
                newS += s[currChar]
                currChar += (numRows - row - 1) * 2 if down else row * 2
                if row != 0 and row != numRows - 1:
                    down = not down
        return newS


print(Solution().convert('A', 1))
