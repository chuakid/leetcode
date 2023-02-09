from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        Sliding window
        """
        if len(p) > len(s):
            return []
        p_map = Counter(p)
        d = {}
        # first pass
        for i in range(len(p)):
            char = s[i]
            if char not in d:
                d[char] = 0
            d[char] += 1
        ans = []
        if d == p_map:
            ans.append(0)
        left, right = 0, len(p)
        while right < len(s):
            d[s[left]] -= 1
            if d[s[left]] == 0:
                del d[s[left]]
            left += 1
            if s[right] not in d:
                d[s[right]] = 0
            d[s[right]] += 1
            if p_map == d:
                ans.append(left)
            right += 1
        return ans
ans = Solution().findAnagrams("cbaebabacd","abc")
assert  ans == [0,6], ans