from math import ceil
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        highest, total = 0, 0
        for pile in candies:
            highest = max(highest, pile)
            total += pile

        def calc(c):
            return sum([pile//c for pile in candies])
        if total < k:
            return 0
        left, right = 1, highest
        while left < right:
            mid = ceil((left+right) / 2)
            if calc(mid) < k:
                right = mid - 1
            else:
                left = mid
        return left


print(Solution().maximumCandies([5, 8, 6], 3))
