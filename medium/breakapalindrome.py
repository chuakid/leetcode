class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 0 or length == 1:
            return ''
        for i, c in enumerate(palindrome[:length//2]):
            if c != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'
