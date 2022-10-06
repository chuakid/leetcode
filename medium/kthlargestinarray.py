class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # quick select
        left = 0
        right = len(nums)
        while True:
            j = left
            for i in range(left + 1, right):
                if nums[i] <= nums[left]:
                    j += 1
                    nums[j], nums[i] = nums[i], nums[j]
            if len(nums) - k == j:
                return nums[left]
            nums[left], nums[j] = nums[j], nums[left]
            if j < len(nums) - k:
                left = j + 1
            else:
                right = j


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
