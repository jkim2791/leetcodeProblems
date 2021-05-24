## https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        ## make a list for every letter in s 
        s = [s for s.lower() in s if s.isalnum]
        ## compare two lists (above list and reversed list)
        return s == s[::-1]

        