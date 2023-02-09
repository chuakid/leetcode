class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        """
        For each pair, they cannot combine to make a new name if they share the same initials or they share the same suffix.
        Thus, to find number of pairs, put each idea into a set based on its initial, then compare it with other sets to find
        non-intersecting pairs and multiply them to get distinct pairs, then multiply by 2 to reverse them.
        """
        sets: list[set] = [set() for _ in range(26)]
        for i in ideas:
            sets[ord(i[0]) - ord('a')].add(i[1:])

        ans = 0
        for i in range(25):
            for j in range(i + 1, 26):
                intersecting_count = len(sets[i].intersection(sets[j]))
                ans += 2 * (len(sets[i]) - intersecting_count) * \
                    (len(sets[j]) - intersecting_count)
        return ans


ans = Solution().distinctNames(["coffee", "donuts", "time", "toffee"])
assert ans == 6
