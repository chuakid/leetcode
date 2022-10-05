class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        # dp[numberofdice][target]
        for i in range(1, target + 1 if k + 1 > target else k+1):
            dp[1][i] = 1
            # 1 way to make any number from 1 to k with 1 die
        for i in range(2, n + 1):
            # for each number of dice from 2 to n
            for tar in range(i, target+1):
                # compute the number of ways to make i to target with i number of dice (cannot make below i with i dice)
                if tar > n * k:  # max for n*k-sided dice == n*k
                    break
                cur = 0
                # number of ways to make tar with i dice == number of ways to make tar - k to tar - 1 with i-1 dice
                for j in range(tar - k if tar - k > 0 else 0, tar):
                    cur += dp[i-1][j]
                dp[i][tar] = cur
        return dp[n][target] % 1000000007


print(Solution().numRollsToTarget(2, 12, 8))
