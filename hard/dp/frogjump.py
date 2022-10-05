import bisect


class Solution:
    def canCross(self, stones) -> bool:
        if stones[1] > 1:
            return False
        stone_count = len(stones)
        if stone_count == 2:
            return True
        dp = [set() for _ in range(stone_count - 1)]
        dp[1].add(1)
        # dp[i] contains the possible k values at dp[i]
        for i in range(1, stone_count - 1):
            for k in dp[i]:
                for j in range(k-1, k+2):
                    if j < 1:
                        continue
                    index = bisect.bisect_left(stones, stones[i] + j, lo=i)
                    if index < stone_count and stones[index] == stones[i] + j:
                        if index == stone_count - 1:
                            return True
                        dp[index].add(j)
        return False
