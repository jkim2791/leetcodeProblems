class Solution(object):
    def isPalindrpme(self, s):
        s = [s for s.lower() in s if s.isalnum]
        return s == s[::-1]