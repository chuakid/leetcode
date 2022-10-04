import bisect


class Solution:
    def answerQueries(self, nums, queries) -> List[int]:
        nums.sort()
        # create prefix array where arr[i] == sum of nums[:i]
        arr = [0]  # 0 for empty sequence
        for i in range(len(nums)):
            arr.append(arr[i] + nums[i])
        ans = []
        for i in queries:
            a = bisect.bisect_right(arr, i) - 1
            ans.append(a)
        return ans
