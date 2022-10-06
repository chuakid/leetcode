import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        # dp[i] = least number of coins required to make i
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    # dp[i - c] = least number of ways to make i - c
                    # dp[i - c] + 1 = least number of ways to make i with one more coin c
                    # deciding which coin to use
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] < math.inf else -1


# print(Solution().coinChange([2], 3))
print(Solution().coinChange([186, 419, 83, 408], 6249))
