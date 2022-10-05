class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dp = {}
        currMax = 0
        for i, v in enumerate(s):
            if v in dp:
                if left < dp[v] + 1:
                    left = dp[v] + 1
            dp[v] = i
            currMax = max(currMax, i - left + 1)
        return currMax


print(Solution().lengthOfLongestSubstring('abba'))
