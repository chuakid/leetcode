from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # nlogn
        ans = []
        for i, v in enumerate(nums[:-2]):
            left, right = i + 1, len(nums) - 1
            if i > 0 and v == nums[i-1]:
                # remove duplicates by not letting i refer to the same value twice
                continue
            while left < right:
                # remove duplicates by not letting left refer to the same value twice
                while left > i+1 and left < right and nums[left] == nums[left-1]:
                    left += 1
                if left == right:
                    break
                if nums[left] + nums[right] + v == 0:
                    ans.append([nums[left], nums[right], v])
                if v + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))

print(Solution().threeSum([0, 0, 0, 0]))
