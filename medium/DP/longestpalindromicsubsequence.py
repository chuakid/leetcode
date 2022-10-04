class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        strlen = len(s)
        dp = [[0 for _ in range(strlen+1)] for _ in range(strlen+1)]
        # dp[left][right] is the length of the longest palindrome subseq from left to right
        # i right edge, j left edge
        # check from right to left edge for palindromes,
        for i in range(0, strlen):
            dp[i][i] = 1
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    # if right == left, then longest from left to right == left+1 to right-1 + 2
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    # else, longest from left to right == max(left+1 to right, left to right - 1)
                    dp[j][i] = max(dp[j+1][i], dp[j][i-1])
        return dp[0][strlen-1]


print(Solution().longestPalindromeSubseq("bbbab"))
