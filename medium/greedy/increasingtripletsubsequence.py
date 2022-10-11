from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest, secondLowest = float('inf'), float('inf')
        for num in nums:
            if num < lowest:
                lowest = num
            elif num < secondLowest and num > lowest:
                secondLowest = num
            elif lowest != secondLowest and num > secondLowest:
                return True
        return False
