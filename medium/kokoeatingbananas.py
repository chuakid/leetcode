from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def calc(k):
            # calculates amount of time needed to eat the piles with k rate
            return sum([ceil(pile / k) for pile in piles])

        # binary search
        while left < right:
            mid = (left+right)//2
            if calc(mid) > h:
                left = mid + 1
            else:
                right = mid
        return right


print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6))
