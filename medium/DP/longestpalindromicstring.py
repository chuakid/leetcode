class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        # for each character in s
        for i, v in enumerate(s):
            # expand around i, treat as center
            for j in range(len(s) - i):
                currLeft, currRight = i-j, i+j
                # if currLeft outside bounds or curr string not palindromic, break
                if currLeft < 0 or s[currRight] != s[currLeft]:
                    break
                # current string is palindromic, check if length > largest palindrome
                if right - left < currRight - currLeft:
                    right, left = currRight, currLeft
            # if i == i+1, expand around i,i+1. Even length palindrome
            if i != len(s) - 1 and v == s[i+1]:
                for j in range(len(s) - i - 1):
                    currLeft, currRight = i-j, i+j+1
                    if currLeft < 0 or s[currRight] != s[currLeft]:
                        break
                    if right - left < currRight - currLeft:
                        right, left = currRight, currLeft
            # Speed check
            if right == len(s) - 1 and left == 0:
                return s
        return s[left:right+1]


print(Solution().longestPalindrome("aacabdkacaa"))
