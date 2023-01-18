from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        d = defaultdict(lambda:0)
        d[0] = 1
        ans = 0
        curr_sum = 0
        # sum up to i - sum up to j = sum between i and j
        # therefore, to find number of subarrays up to i that add up to k, I just need to find number of subarrays up to i that
        # sum up to (sum up to i) - k
        for i in nums:
            curr_sum += i
            ans += d[curr_sum - k]
            d[curr_sum] += 1
        return ans
print(Solution().subarraySum([1,1,1], 2))