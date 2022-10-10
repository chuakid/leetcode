class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack:
                if stack[-1][0] == c:
                    stack[-1][1] += 1
                else:
                    stack.append([c, 1])
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()
        ans = ''
        for i in stack:
            ans += i[0] * i[1]
        return ans
